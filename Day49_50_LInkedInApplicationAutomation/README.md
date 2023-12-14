# LinkedIn Auto Apply App

This project is normally only day 49, but because day 50 was a tinder bot that I wasn't very interested in creating, I decided to add much more functionality that in the courses requirements for this app and count it for both days. The app utilizes a given search link from linked in and will apply to all "EZ Apply" capable jobs in that search.

The original requirements for this project were to apply to a row of search results, and only the ones that had an extremely simple, single window for their "EZ Apply". To extend my project as a two day task, I added much more functionality. Specifically the app will:
- After automaticaly logging in, will wait for me to hit enter in case there is a captcha verification that I need to sort manually
- Will apply to any complexity of EZ Apply jobs
- Will notify me through Windows notifications if there are any fields that it cannot fill out automatically
- Able to continue automation after I fill the information that caused it to notify me.
- Is able to automatically discard an EZ apply if I tell it to not continue with the current application after a notification.
- Will traverse all pages of search results, instead of just the one row.

It took me quite a while, but because this felt like a really useful app for me, it was really fun to work out all the problems. One issue that popped up in all the Selenium projects so far was the "Stale Element" error when trying to find anything after changes such as clicking a button or loading a new window. Adding sleep timers helped, but it became such a nuisance that I ended up creating a new method for button clicks called `safe_click()` that would loop over a `click()` within a `try` statement, and only return when there was finally no error.
