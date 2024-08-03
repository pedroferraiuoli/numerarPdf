from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import os
from django.contrib import messages
from reportlab.pdfgen import canvas
from PyPDF2 import PdfWriter, PdfReader

class NumerarPdfView(TemplateView):
    template_name = 'numerador/numerarPdf.html'

    def post(self, request):
        if request.FILES.get('pdf_file'):
            try:
                uploaded_file = request.FILES['pdf_file']
                posicao = request.POST.get('posicao')
                pagina = int(request.POST.get('pagina'))
                fs = FileSystemStorage()
                filename = fs.save(uploaded_file.name, uploaded_file)
                uploaded_file_path = fs.path(filename)

                numbered_pdf_path = self.generate_numbered_pdf(uploaded_file_path, posicao, pagina)

                with open(numbered_pdf_path, 'rb') as f:
                    response = HttpResponse(f.read(), content_type='application/pdf')
                    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(numbered_pdf_path)}"'
                os.remove(uploaded_file_path)
                os.remove(numbered_pdf_path)
                return response
            except Exception:
                messages.warning(request, 'Erro! Tente novamente')
                return redirect("/")

    def create_page_pdf(self, num, tmp, page_sizes, pagina, posicao=None):

        c = canvas.Canvas(tmp, pagesize=page_sizes[0])

        for i in range(1, num + 1):
            if i >= pagina:
                largura, altura = page_sizes[i - 1]
                lar, alt = float(largura), float(altura)
                c.setFont('Helvetica', 22)

                positions = {
                    'dsup': (lar - 30, alt - 30),
                    'dinf': (lar - 30, 30),
                    'esup': (30, alt - 30),
                    'einf': (30, 30)
                }

                x, y = positions.get(posicao, (lar - 30, alt - 30))
                c.drawString(x, y, str(i))
            c.showPage()
        c.save()

    def generate_numbered_pdf(self, pdf_path, posicao, pagina):
        tmp_path = "__tmp.pdf"
        with open(pdf_path, 'rb') as f:
            pdf = PdfReader(f)
            n = len(pdf.pages)
            page_sizes = [(page.mediabox.width, page.mediabox.height) for page in pdf.pages]

            self.create_page_pdf(n, tmp_path, page_sizes, pagina, posicao)

            output = PdfWriter()
            with open(tmp_path, 'rb') as ftmp:
                numberPdf = PdfReader(ftmp)
                for p in range(n):
                    page = pdf.pages[p]
                    numberLayer = numberPdf.pages[p]
                    page.merge_page(numberLayer)
                    output.add_page(page)

                new_pdf_path = pdf_path.replace('.pdf', '_numerado.pdf')
                with open(new_pdf_path, 'wb') as f:
                    output.write(f)

        os.remove(tmp_path)
        return new_pdf_path
