import io
from django.http import FileResponse, HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the ledger index.")


def invoice_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    create_invoice_pdf(buffer)
    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")
