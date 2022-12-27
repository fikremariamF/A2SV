class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_dictionary = {}
        for domain in cpdomains:
            domain= domain.split()
            domain_count = int(domain[0])
            split_domains = domain[1].split('.')
            for i in range(len(split_domains)-1,-1, -1):
                specific_domain = []
                for i in split_domains[i:]:
                    if specific_domain:
                        specific_domain.append(".")
                    specific_domain.append(i)
                specific_domain= "".join(specific_domain)
                domain_dictionary[specific_domain] = domain_dictionary.get(specific_domain,0) + domain_count
        output = []
        for key in domain_dictionary:
            output.append(str(domain_dictionary[key]) + " " + key)
        return output