# 📒 Contact Book

A fully-featured command-line contact manager built in Python.
Contacts are stored as JSON and persist automatically between sessions —
every change is saved instantly, so no data is ever lost.

Built as the Month 2 capstone project of a 12-month Python learning roadmap,
this is the most architecturally complete project in the series — structured
across five dedicated files following strict separation of concerns.

![demo](assets/demo.gif)

---

## ✨ Features

### Core CRUD Operations
- **Add** a contact with full field-by-field validation
- **View all** contacts displayed alphabetically in a clean formatted layout
- **Search** by name, email or phone number — partial search supported
- **Edit** any individual field of any contact with re-validation
- **Delete** a contact with explicit confirmation prompt

### Advanced Features
- **Favourites system** — toggle any contact as a favourite, view all favourites
- **Category views** — browse contacts grouped by Family, Friend, Work, School or Other
- **Statistics page** — total contacts, category breakdown, most recent addition, contacts added this month
- **Export to .txt** — generate a clean human-readable export file with a timestamped header
- **Pagination** — contacts display 10 at a time for large collections

### Data Integrity
- Automatic JSON persistence on every single change — no manual saving required
- Graceful handling of missing or corrupted data files on startup
- Duplicate detection for names, phone numbers and email addresses
- Full input validation on every field with specific error messages per failure

---

## 🗂 Project Structure

```
contact-book/
├── main.py                  # Entry point — main loop and menu dispatcher
├── contacts.py              # All contact operations (add, edit, delete, search)
├── validation.py            # All input validation functions
├── file_handler.py          # JSON load and save logic
├── display.py               # All formatted terminal output
├── contacts_example.json    # Sample data demonstrating the expected structure
├── .gitignore
├── README.md
└── LICENSE
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- No external dependencies — standard library only

### Installation & Run

```bash
git clone https://github.com/ERYXGF/contact-book.git
cd contact-book
python main.py
```

On first run the program creates `contacts.json` automatically.
To start with sample data, rename `contacts_example.json` to `contacts.json`
before running.

---

## 🕹 How to Use

Run `python main.py`. The main menu displays the current contact count and
all available options. Navigate by entering the corresponding number.
Every action confirms success or explains failure before returning to the menu.

```
╔══════════════════════════════════════╗
║         📒 CARNET DE CONTACTS       ║
║         12 contacts enregistrés     ║
╚══════════════════════════════════════╝

  1. Voir tous les contacts
  2. Ajouter un contact
  3. Rechercher un contact
  4. Modifier un contact
  5. Supprimer un contact
  6. Voir les favoris
  7. Voir par catégorie
  8. Statistiques
  9. Exporter en .txt
  0. Quitter
```

---

## 📋 Validation Rules

Every field is validated before saving. The rules enforced are:

| Field | Rules |
|---|---|
| Name | Two words minimum, letters and spaces only, no duplicates |
| Phone | 7–15 digits, allows spaces / hyphens / +, no duplicates |
| Email | Must contain @ and a domain dot, no duplicates |
| City | Letters, spaces and hyphens only |
| Category | Selected from predefined list — never free text |

---

## 📁 Data Structure

Contacts are stored in `contacts.json` as a dictionary of dictionaries.
The key is the lowercased full name for case-insensitive lookup:

```json
{
    "alice martin": {
        "name": "Alice Martin",
        "phone": "+33 06 12 34 56 78",
        "email": "alice.martin@gmail.com",
        "city": "Toulouse",
        "category": "Friend",
        "favourite": true,
        "date_added": "2025-03-09"
    }
}
```

---

## 🛠 Built With

- Python 3.11
- Standard library only — `json`, `os`, `datetime`

---

## 📚 What I Learned

- Architecting a project across multiple files using strict separation of concerns
- Building a complete CRUD application with persistent state
- Designing and enforcing comprehensive input validation across all fields
- Working with nested dictionaries to represent structured real-world data
- Using JSON for automatic data persistence with graceful error handling
- Implementing partial search across multiple fields simultaneously
- Paginating large data sets for a clean terminal user experience
- Writing modular, reusable functions that each do exactly one thing
- Complex maniuplation of dictionnaries
- How to plan and build a complex project with more than 500 lines of code
- How to structure a project of such complexity

---

## 🗺 Future Improvements

- [ ] Add birthday field with upcoming birthday alerts
- [ ] Sort contacts by different fields (city, category, date added)
- [ ] Import contacts from a CSV file
- [ ] Add a notes field for free-form text per contact
- [ ] Password-protect the contact book on startup

---

## ⚠️ Privacy Note

`contacts.json` and `contacts_export.txt` are excluded from version control
via `.gitignore` as they may contain real personal data. The included
`contacts_example.json` contains entirely fictional data for demonstration
purposes only.

---

## 📄 Licence

This project is licensed under the GPL-3.0 Licence.
See the [LICENSE](LICENSE) file for details.

---

*Project 2 of 12 — Python learning roadmap | Built by [Eryx Grammatikas](https://github.com/ERYXGF)*