import pandas as pd

quiz_questions = [
    ["Mi a PyCharm elsődleges célja a Python fejlesztés során?", "Egy integrált fejlesztői környezet biztosítása, eszközökkel a Python kód írásához és teszteléséhez.", "Python kód fordítása végrehajtható fájlokká.", "Python verziók és környezetek kezelése további eszközök nélkül.", "A Python végrehajtási sebességének növelése."],
    ["Melyik Python adatszerkezetet használják elsősorban kulcs-érték párok tárolására?", "Szótárak", "Listák", "Tuple-ok", "Halmazok"],
    ["Mi a Pandas könyvtár elsődleges felhasználási területe Pythonban?", "Adatmanipulációra és elemzésre.", "Python webalkalmazások készítésére.", "Asztali GUI alkalmazások fejlesztésére.", "Gépi tanulásra."],
    ["Mi az egyik előnye a ChatGPT használatának adatfeldolgozási feladatok során?", "Segíthet Python kód generálásában adatelemzéshez.", "Helyettesítheti az összes hagyományos adatfeldolgozási eszközt.", "Automatikusan kijavít minden adathibát.", "Megszünteti a programozási tudás szükségességét."],
    ["Hogyan lehet az OpenAI API-t felhasználni egy projektben?", "AI-alapú funkciók, mint a szöveggenerálás, alkalmazásokba való integrálása.", "Közvetlenül Python scripteket futtatni az OpenAI szerverein.", "Helyi Python telepítések helyettesítésére.", "Automatikus kódellenőrzések végrehajtására emberi beavatkozás nélkül."],
    ["Mi a listák elsődleges funkciója Pythonban?", "Több elem tárolása egyetlen változóban.", "Kulcs-érték párok tárolása.", "Python parancsok sorozatának végrehajtása sorrendben.", "Adatmanipulációs szabályok meghatározása."],
    ["Hogyan lehet egy új kulcs-érték párt hozzáadni egy meglévő szótárhoz Pythonban?", "Egy új kulcshoz érték hozzárendelésével a szögletes zárójelek használatával.", "Az `add()` metódus használatával.", "Az `append()` metódus segítségével.", "A `insert()` funkcióval."],
    ["A Python fájlkezelés kontextusában mit csinál a 'w' mód?", "Csak írásra nyitja meg a fájlt, létrehozza a fájlt, ha az nem létezik, vagy törli a tartalmát, ha már létezik.", "Csak olvasásra nyitja meg a fájlt.", "Írásra és olvasásra is megnyitja a fájlt.", "Hozzáfűzési módban nyitja meg a fájlt, lehetővé téve új adatok hozzáadását a meglévő tartalomhoz."],
    ["Melyik funkciót használják általában egy string datetime objektummá konvertálására Pythonban?", "strptime()", "strftime()", "to_datetime()", "parse()"],
    ["Melyik módszer a gyakori az idő és dátum adatok kezelésére Pandasban?", "Stringek datetime objektummá konvertálása a pd.to_datetime() segítségével.", "Közvetlenül a datetime modul használata.", "A DataFrame-en a time() funkció hívása.", "A date_range() metódus használata dátumok generálására."],
    ["Mi a groupby() metódus célja Pandasban?", "Adatok csoportosítása egy vagy több oszlop alapján és műveletek végrehajtása minden csoporton.", "Több DataFrame összefűzése.", "Egy DataFrame rendezése egy bizonyos oszlop alapján.", "Két DataFrame egyesítése egy közös kulcs alapján."],
]

quiz_df = pd.DataFrame(quiz_questions, columns=["Question", "Correct Answer", "Incorrect Answer 1", "Incorrect Answer 2", "Incorrect Answer 3"])

csv_file_path = "quiz_questions.csv"

# Convert the DataFrame into a CSV file
quiz_df.to_csv(csv_file_path, index=False)
