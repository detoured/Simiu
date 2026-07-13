from PIL import Image, ImageDraw, ImageFont
import imagehash
import sys
import argparse

def swap(domain,tld,urls):
    for i in range(len(domain) - 1):
        tmp_domain = list(domain)
        tmp = tmp_domain[i]
        tmp_domain[i] = tmp_domain[i+1]
        tmp_domain[i+1] = tmp
        urls.append("".join(tmp_domain)+f".{tld}")

def repetition(domain,tld,urls):
    for i in range(len(domain)):
        urls.append(domain[:i] + domain[i] * 2 + domain[i+1:] + f".{tld}")

def omission(domain,tld,urls):
    for i in range(len(domain)):
        urls.append(domain[:i] + domain[i+1:] + f".{tld}")

def render_text(url):
    size=(400, 80)
    font_size=32
    url_img = Image.new("RGB",size, color='white')
    draw = ImageDraw.Draw(url_img)
    
    font = ImageFont.truetype("ARIAL.TTF", font_size)

    draw.text((10, 10), url, fill='black', font=font)

    return url_img

def get_phash(img):
    return imagehash.phash(img)

def compare_phashes(pash1,pash2):
    return pash1 - pash2

def get_similar_url_phashes(urls):
    url_to_phash = []
    for i in range(0,len(urls)):
        url_to_phash.append({"url":urls[i],"phash":get_phash(render_text(urls[i]))})

    return url_to_phash

def compare_similar_phashes(similar_phashes,original_phash):
    similarity = []
    for i in range(0, len(similar_phashes)):
        similarity.append({"url":similar_phashes[i]["url"],"value":int(compare_phashes(similar_phashes[i]["phash"],original_phash))})

    return similarity

def normalize_results(sorted_data):
    results = []
    for i in range(0,len(sorted_data)):
        results.append(f"{i+1}. {sorted_data[i]["url"]}") 

    return "\n".join(results)

def handle_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("url",type=str,help="url to mimic")
    parser.add_argument("-l","--log",type=str,help="log the output to a specified txt file (-l/--log <file.txt>)")
    args = parser.parse_args()

    if not args.url:
        sys.exit("A url must be provided")
    
    if args.log and args.log.rsplit(".",1)[1] != "txt":
        sys.exit("Log file must be a txt file")

    return args

def log_output(args,results):
    with open(args.log,"w") as file:
        file.write(results)

def main():
    args = handle_args()
    original_url = args.url
    
    domain = original_url.rsplit(".",1)[0]
    tld = original_url.rsplit(".",1)[1]
    similar_urls = []

    swap(domain,tld,similar_urls)
    repetition(domain,tld,similar_urls)
    omission(domain,tld,similar_urls)
    
    original_url_img = render_text(original_url)
    original_url_phash = get_phash(original_url_img)

    url_to_phash = get_similar_url_phashes(similar_urls)
    similarity = compare_similar_phashes(url_to_phash,original_url_phash)

    sorted_similarity = sorted(similarity, key=lambda x: x["value"])
    results = normalize_results(sorted_similarity)
    print(results)

    if args.log:
        log_output(args,results)

main()