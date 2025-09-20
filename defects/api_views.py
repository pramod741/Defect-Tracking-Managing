from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Developers, Testers, DefectDetails, Defect_Screen_Shots
from .serializers import (
    DeveloperSerializer, TesterSerializer, DefectSerializer, ScreenshotSerializer
)

# ---------- Developers ----------
@api_view(['GET', 'POST'])
def developers_list(request):
    if request.method == 'GET':
        devs = Developers.objects.all()
        serializer = DeveloperSerializer(devs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DeveloperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---------- Testers ----------
@api_view(['GET', 'POST'])
def testers_list(request):
    if request.method == 'GET':
        testers = Testers.objects.all()
        serializer = TesterSerializer(testers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TesterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---------- Defects ----------
@api_view(['GET', 'POST'])
def defects_list(request):
    if request.method == 'GET':
        defects = DefectDetails.objects.all()
        serializer = DefectSerializer(defects, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DefectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def defect_detail(request, id):
    try:
        defect = DefectDetails.objects.get(id=id)
    except DefectDetails.DoesNotExist:
        return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DefectSerializer(defect)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DefectSerializer(defect, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        defect.delete()
        return Response({"message": "Deleted"}, status=status.HTTP_204_NO_CONTENT)


# ---------- Screenshots ----------
@api_view(['GET', 'POST'])
def screenshots_list(request):
    if request.method == 'GET':
        shots = Defect_Screen_Shots.objects.all()
        serializer = ScreenshotSerializer(shots, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ScreenshotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
