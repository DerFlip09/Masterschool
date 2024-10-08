import re

log_file = """
*.amazon.co.uk    89
*.doubleclick.net    139
*.fbcdn.net    212
*.in-addr.arpa    384
*.l.google.com    317
1.client-channel.google.com    110
6.client-channel.google.com    45
a.root-servers.net    1059
apis.google.com    43
clients4.google.com    71
clients6.google.com    81
connect.facebook.net    68
edge-mqtt.facebook.com    56
graph.facebook.com    150
mail.google.com    128
mqtt-mini.facebook.com    47
ssl.google-analytics.com    398
star-mini.c10r.facebook.com    46
staticxx.facebook.com    48
www.facebook.com    178
www.google.com    162
www.google-analytics.com    127
www.googleapis.com    87
"""


def get_log_list(log_file):
    return log_file.strip().split("\n")


def get_domains(log_file):
    return re.findall(r"\w+-?\w+(?:\.\w\w)?\.\w+ ", log_file)


def get_freq_dict(log_file):
    freq_dict = {}
    unique_domains = set(get_domains(log_file))
    log_file_list = get_log_list(log_file)
    for domain in unique_domains:
        freq_list = [log for log in log_file_list if domain in log]
        for item in freq_list:
            subdomain, freq = item.split()
            if domain in freq_dict:
                freq_dict[domain] += int(freq)
            else:
                freq_dict[domain] = int(freq)
    return freq_dict


def count_domains(log_file, min_hits):
    freq_dict = sorted(get_freq_dict(log_file).items(), key=lambda k: k[1], reverse=True)
    domain_freq_list = [f"{domain} ({freq})" for domain, freq in freq_dict
                        if freq >= min_hits]
    return "\n".join(domain_freq_list)


def get_min_hits():
    """
    Prompts the user to enter a minimum number of hits for a domain.

    :returns: Positive integer representing the minimum number of hits.
    """
    while True:
        try:
            min_hits = int(input("Enter the minimal hits for a domain: "))
        except ValueError:
            print("Please enter a positive number!")
            continue
        if min_hits < 0:
            print("Please enter a positive number!")
            continue
        return min_hits


def main():
    min_hits = get_min_hits()
    print(count_domains(log_file, min_hits))


if __name__ == "__main__":
    main()
