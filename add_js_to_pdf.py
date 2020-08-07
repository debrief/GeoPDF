import pikepdf
from pikepdf import Pdf, OutlineItem


with Pdf.open('TampaFD_TemporalPDF-4.pdf') as pdf:
    with pdf.open_outline() as outline:
        new_action = pikepdf.Dictionary()
        new_action['/S'] = pikepdf.Name('/JavaScript')
        new_action['/JS'] = "app.alert(\"Hello from Robin\");"
        test_item = OutlineItem('Test Alert Robin', action=new_action)
        outline.root.append(test_item)
    pdf.save('output1.pdf')