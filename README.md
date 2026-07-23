# **Simiu**

Simiu generates similar urls to a provided one and outputs a list that ranks them using perceptual hashing

---

## **Installation**

```bash
# Clone the repository
git clone https://github.com/detoured/Simiu.git

# Navigate to the Simiu directory
cd Simiu

# Sync uv
uv sync
```

---

## **Usage**

```
uv run main.py <url> [-l <file>] [-a]
```

---

## **Flags**

- -l/--log: log the output to a specified txt file (-l/--log <file_name>)
- -a/--availability: include domain status (available / not available) in output
---