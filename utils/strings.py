import re


def normalize_whitespace(string: str) -> str:
    return " ".join(string.split())


def safe_truncate(string: str, n: int) -> str:
    truncated = string[0: n]

    matches_original = re.finditer(r"\w+", string)
    matches_trunc = re.finditer(r"\w+", truncated)

    for (m_trunc, m_org) in zip(matches_trunc, matches_original):
        if m_trunc.group() != m_org.group():
            mut_string = list(truncated)
            mut_string[m_trunc.start():m_trunc.end()] = m_org.group()
            return "".join(mut_string).strip()

    return truncated.strip()
