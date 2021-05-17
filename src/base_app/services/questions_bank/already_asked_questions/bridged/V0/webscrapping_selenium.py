from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
url ="https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:A/AC:H/PR:L/UI:R/S:C/C:L/I:L/A:L"

d = webdriver.Chrome(chrome_options=chrome_options)
d.get(url)
print(d.find_element_by_css_selector("#cvss-overall-score-chart > div.jqplot-point-label.jqplot-series-0.jqplot-point-0").text)
d.quit()
