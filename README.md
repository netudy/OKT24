# Programmering 1 - Git Övning

Välkommen till övningen för kursen **Programmering 1**!

## Syfte

Denna övning syftar till att ge dig praktisk erfarenhet av att arbeta med Git. Du kommer att:
- Klona ett repository
- Skapa en ny branch
- Ändra och committa i en README.md fil
- Lägga till din lärare som reviewer
- Skapa en pull request

## Instruktioner

### 1. Klona Repositoryt
Klona repot till din lokala maskin med följande kommando:

    git clone git@github.com:netudy/OKT24.git

### 2. Skapa en Ny Branch
Skapa en ny branch där du ska göra dina ändringar:

    git checkout -b din-branch-namn

### 3. Redigera README.md
Öppna filen `README.md` och gör följande ändringar:
- Lägg till en beskrivning som berättar att detta repository används för kursen **Programmering 1**.
- Förbättra filens format med rubriker, listor och andra markdown-element.
- Ange kortfattat vad dina ändringar handlar om.

### 4. Committa Ändringarna
Lägg till filen och skapa en commit med ett beskrivande meddelande:

    git add README.md
    git commit -am "motivera varför du gjort följande ändringar"

### 5. Push Branch
Skicka din nya branch till GitHub:

    git push origin din-branch-namn

### 6. Skapa en Pull Request
- Gå till GitHub och skapa en pull request från din branch mot `main`-branchen.
- Lägg till din lärare som reviewer.
- Skriv en kort beskrivning av dina ändringar.

## Checklista
- [ ] Repositoryt är klonat korrekt
- [ ] En ny branch har skapats och används
- [ ] README.md har uppdaterats med kursinformation och instruktioner
- [ ] Ändringarna är committade och pushade
- [ ] En pull request har skapats med lärare som reviewer

Lycka till med övningen!
