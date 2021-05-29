from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from vehiclelanedetection.settings import BASE_DIR
from .process_image import *
# Create your views here.


class Findlane(APIView):

    def get(self, request, format=None):
        snippets = FindLane.objects.all()
        serializer = FindLaneSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        input_img_file = request.FILES['input_img']
        # input_img_file =str(input_img_file.read())
        # Image.open(os.path.join(PATH, filename))
        img = cv2.imread(open(Image.open(os.path.join(PATH, filename))))
        cropped_img = area_of_interest(img, [crop_points.astype(np.int32)])
        trans_img = applyTransformation(cropped_img)
        masked_image = applyMasks(trans_img)
        left_fit, right_fit, _ = slidingWindow(masked_image)
        lane_mask = applyBackTrans(img, left_fit, right_fit)
        img_result = cv2.addWeighted(img, 1, lane_mask, 1, 0)
        serializer = FindLaneSerializer(data={'input_img':input_img_file, 'output_img':img_result})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

