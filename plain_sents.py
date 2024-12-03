# eff it, thucy time

from lxml import etree
from MyCapytain.common.constants import Mimetypes
from MyCapytain.resources.texts.local.capitains.cts import CapitainsCtsText
import pandas as pd

with open("tei/tlg0003.tlg001.perseus-grc2.xml") as f:
    text = CapitainsCtsText(urn="urn:cts:greekLit:tlg0003.tlg001.perseus-grc2", resource=f)

urns = []
raw_xmls = []
unannotated_strings = []

for ref in text.getReffs(level=len(text.citation)):
    urn = f"{text.urn}:{ref}"
    node = text.getTextualNode(ref)
    raw_xml = node.export(Mimetypes.XML.TEI)
    tree = node.export(Mimetypes.PYTHON.ETREE)
    s = etree.tostring(tree, encoding="unicode", method="text")

    urns.append(urn)
    raw_xmls.append(raw_xml)
    unannotated_strings.append(s)

d = {
    "urn": pd.Series(urns, dtype="string"),
    "raw_xml": raw_xmls,
    "unannotated_strings": pd.Series(unannotated_strings, dtype="string")
}
history_df = pd.DataFrame(d)

for u in unannotated_strings:
    print(u.replace("\n", " ").replace("\t", " "))
