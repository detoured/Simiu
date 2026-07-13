def main():
    url = "google.com"
    domain = url.rsplit(".",1)[0]
    tld = url.rsplit(".",1)[1]
    similar_urls = []
    repetition(domain,tld,similar_urls)
    print(similar_urls)

def swap(url,similar_urls):
    domain = url.rsplit(".",1)[0]
    tld = url.rsplit(".",1)[1]
    for i in range(len(domain) - 1):
        tmp_domain = list(domain)
        tmp = tmp_domain[i]
        tmp_domain[i] = tmp_domain[i+1]
        tmp_domain[i+1] = tmp
        similar_urls.append("".join(tmp_domain)+f".{tld}")

def repetition(domain,tld,similar_urls):
    for i in range(len(domain)):
        similar_urls.append(domain[:i] + domain[i] * 2 + domain[i+1:] + f".{tld}")

main()