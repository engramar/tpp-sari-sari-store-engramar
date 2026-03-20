# M01 Concept Check — Input, Output, at Variables

_Taglish lang tayo pero siguraduhin mong malinaw at kumpleto ang paliwanag. Palitan ang `{{ISULAT_DITO}}` gamit ang sarili mong sagot (≥ 2 sentences)._ 

## 1. Bakit mahalaga ang maayos na pag-cast (e.g., `int`, `float`) sa sari-sari store receipt?
**Sagot ko:** Mahalaga ang tamang pag-cast dahil ang `input()` sa Python ay palaging nagre-return ng string, pero para sa receipt kailangan natin ng numbers para sa price, quantity, total, at change. Kung hindi natin i-cast sa `float`, ang "20" * "3" ay magiging string concatenation imbes na multiplication, at mali ang computation. Sa sari-sari store, may mga item na may decimal price (e.g., 12.50), kaya `float` ang dapat gamitin para accurate ang sukli.

## 2. Ano ang pinagkaiba ng "raw input" at "clean data" sa konteksto ng module na ito?
**Sagot ko:** Ang "raw input" ay yung literal na kinuha natin mula sa user—string pa lahat, may spaces o walang spaces, at hindi pa natin alam kung valid. Ang "clean data" naman ay yung na-process na natin: na-strip na ang whitespace, na-convert na sa tamang type (int/float), at ready na para sa computation. Halimbawa, raw input na "  20  " ay magiging clean data na 20.0 (float) pagkatapos ng processing.

## 3. Paano mo ipapaliwanag sa kaibigan ang konsepto ng "state" ng isang CLI app gamit ang inventory ng tindahan bilang halimbawa?
**Sagot ko:** Ang "state" ay parang memory ng app—yung mga variables na nagho-hold ng current info habang tumatakbo ang program. Sa inventory ng tindahan, ang state ay yung listahan ng items, quantities, at prices na naka-store sa variables. Kapag may bumili, nagbabago ang state (bumababa ang stock). Kapag nag-restock, nagbabago ulit. Ang CLI app ay nagre-remember lang ng state sa RAM; kapag nag-exit, nawawala unless i-save sa file.

## 4. Kung rerefactor mo ang `main.py`, anong variable names o sections ang pinaka-kritikal panatilihing malinaw at bakit?
**Sagot ko:** Ang pinaka-kritikal ay yung variables na involved sa computation: `price`, `qty`, `total`, `cash`, at `change`. Dapat malinaw ang names para maintindihan agad kung ano ang ginagawa ng formula (e.g., `total = price * qty`). Mahalaga rin ang separation ng sections—input gathering, computation, at output/printing—para madaling i-debug at i-extend. Kung magulo ang naming, madaling magkamali sa formula lalo na sa sukli calculation.
