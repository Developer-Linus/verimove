from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .services import ALPRProcessing
from .serializers import GateCaptureSerializer

class ALPRCaptureAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        serializer = GateCaptureSerializer(data=request.data)
        if serializer.is_valid():
            plate = serializer.validated_data['plate_number']
            image = serializer.validated_data['image']

            msg = ALPRProcessing.process_capture(plate, image)
            return Response(
                {"detail": msg},
                status=status.HTTP_200_OK
                            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

