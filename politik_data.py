'''
Getting data from the budget from the official pdf file

moderaternas budgetmotion för 2022 (https://www.riksdagen.se/sv/dokument-lagar/dokument/motion/okad-trygghet-och-fler-som-arbetar---moderaternas_H9024040)
'''

import tabula
import pandas as pd

#Moderaternas budgetmotion för 2022
pdf_path = ".\data\mot_202122__4040.pdf"

dfs = tabula.read_pdf(pdf_path, pages="all", lattice = True)

print (len(dfs))

print (dfs[-1])