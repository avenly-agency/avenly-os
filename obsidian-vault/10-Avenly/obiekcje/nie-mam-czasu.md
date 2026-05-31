---
crm:
  table: knowledge_base
  category: obiekcje
  slug: nie-mam-czasu-teraz
  title: "Obiekcja: Nie mam czasu teraz"
  ai_chatbot: true
  is_published: true
---

# Nie mam czasu teraz

**Co naprawdę mówi:** prawdziwie zajęty albo deprioritized.

**Strategia:** kalibracja terminu (data z przyszłości w kalendarzu).

**Skrypt:**

> _Spoko, rozumiem. Kiedy mogę napisać ponownie żeby Cię nie przegapić w gorszym momencie? Październik? Listopad? Po sezonie?_

Wzięcie konkretnej daty w przyszłości — wraca w kalendarzu, NIE w stosie maili. Stwórz task w CRM (`/api/agent/tasks`) z `due_date` na uzgodnioną datę + 7 dni.
