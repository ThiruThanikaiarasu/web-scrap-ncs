from bs4 import BeautifulSoup 
import requests
import pandas as pd

def getData(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    empty_dict = {
    'Title' : [],
    'Company' : []
}

    for i in range(0, 10):  # Change the range to include all the IDs you need
    # Construct the ID for the current iteration
    current_id = f"ctl00_SPWebPartManager1_g_5f765d3f_f705_4af4_83e7_cd16b175ab26_ctl00_rptSearchJobs_ctl{i:02}_lblJobTitle"
    current_company_id = f"ctl00_SPWebPartManager1_g_5f765d3f_f705_4af4_83e7_cd16b175ab26_ctl00_rptSearchJobs_ctl{i:02}_lblOrganization"
    
    # Find the <span> element with the current ID
    span_title = soup.find('span', id=current_id)
    span_company = soup.find('span', id=current_company_id)
    
    # Check if the <span> element is found
    if span_title and span_company:
        # Extract and print the text content from the <span> element
        title_text = span_title.get_text(strip=True)
        company_text = span_company.get_text(strip=True)
        empty_dict['Title'].append(title_text)
        empty_dict['Company'].append(company_text)
        print('Title')
        print(title_text)
        print('Company')
        print(company_text)
    else:
        print(f"Element with ID '{current_id}' not found.")
        print(f"Element with ID '{current_company_id}' not found.")
        print("  ")

    df = pd.DataFrame(empty_dict)
    df.to_json("output.json", orient="records")
    print(empty_dict)

getData('')