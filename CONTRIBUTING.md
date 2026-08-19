# Contributing

## Before changing the template

1. Create a branch.
2. Keep examples fictional and portable.
3. Do not add user-specific paths, private URLs, customer artifacts, or secrets.
4. Keep external actions disabled unless the user explicitly invokes them.

## Required checks

```powershell
python scripts\validate_template.py
python -m unittest discover -s tests -v
```

Pull requests should state:

- the experiment or user outcome being improved;
- the files and behaviors changed;
- whether any external action was added or modified;
- the validation commands and results;
- the privacy review performed on committed examples.

Changes that deploy, publish, register, message, or write to an operational
system must remain separately invoked and clearly documented.
