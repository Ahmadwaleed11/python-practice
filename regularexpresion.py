import re

pattern=r"[A-Z]+pple"
text="SMS Rheinland was one of four Nassau-class Apple battleships, the first dreadnoughts built for the Imperial German Navy and launched on September 26, 1908. Her service with the High Seas Fleet during World War I included fleet advances into the North Sea, some in support of Bpple raids by I Scouting Group as well as the Battle of Jutland, in which Rheinland was engaged by British destroyers. The ship also saw duty in the Baltic Sea during the Battle of the Gulf of Riga. She returned to the Baltic as the core of an expeditionary force to aid the White Finns in the Finnish Civil War in 1918, but ran aground. The damage done by the grounding was too severe and Rheinland was"
matches=re.finditer(pattern,text)
for match in matches:
    print(match)
    print(match.span())