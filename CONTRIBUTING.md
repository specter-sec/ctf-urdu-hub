# Contributing

Shukriya — clear, respectful learning notes welcome hain. Is repository mein contribution karke aap [Code of Conduct](CODE_OF_CONDUCT.md) aur [Ethics & Safe Practice](docs/ethics.md) follow karne par razi hote hain.

## Before opening a pull request

- Naya example fictional, offline, deterministic, and safe-to-run hona chahiye; real people, live services, credentials, private data, or real challenge flags include na karein.
- Har technical claim ko a reliable source se verify karke cite karein. Official documentation or a free platform topic page is preferred; challenge answers or another author's writeup copy na karein.
- Writeups ke liye [standard template](docs/template.md) use karein. Roman Urdu/Hinglish simple, respectful, and readable rakhein; established technical terms ki English spelling preserve karein.
- Local links and image assets repository ke andar rakhein. Remote font, tracker, externally hosted script, or unapproved binary add na karein.
- Tests ke commands aur expected effects explain karein. File-writing examples apne fixed `labs/work/` subdirectory mein confine hon.

## Validate locally

Python 3.11+ and Node.js 22+ use karein. Virtual environment active ho:

```sh
python -m pip install -r requirements.txt
npm ci
npm run lint
python -m unittest discover -s tests -v
python scripts/check_content.py
mkdocs build --strict
```

Agar incoming content abhi incomplete hai to content checker required page ke missing hone par fail karega — failure ko chhupane ke bajaye page complete karein. Screenshots tabhi add karein jab woh actual rendered site se capture kiye gaye hon.

## Pull request checklist

- [ ] Change authorized and safe-to-run hai.
- [ ] Roman Urdu/English copy proofread ki gayi hai.
- [ ] Source, scope, and limitations clear hain.
- [ ] Local links, frontmatter, and assets check kiye gaye hain.
- [ ] Lint, tests, content checker, and strict build pass.
- [ ] Screenshot reference update ho to actual screenshot committed hai.
