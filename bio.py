from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from googletrans import Translator
import os



def getBio(iterator):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://www.character-generator.org.uk/bio/')

    driver.implicitly_wait(5)

    driver.find_element_by_xpath('//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]').click()

    try:
        random_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="fill_all"]')))
        random_input.click()
    except:
        print("Cos poszło nie tak przy wypelnianiu :'(")

    isMale = driver.find_element_by_xpath('//*[@id="main"]/div/form/input[9]').is_selected()
    # isFemale = driver.find_element_by_xpath('//*[@id="main"]/div/form/input[10]').is_selected()

    try:
        generate_bio = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/form/input[29]')))
        generate_bio.click()
    except:
        print("Cos poszło nie tak przy generowaniu :'(")

    biography = driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div').text

    print(biography)

    # driver.get('https://www.deepl.com/pl/translator')

    # driver.find_element_by_xpath('//*[@id="dl_translator"]/div[3]/div[2]/div[1]/div[2]/div/textarea').send_keys(
    #     biography
    # )
    # sleep(5)
    # try:
    #     # pl_biography = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dl_translator"]/div[3]/div[2]/div[3]/div[3]/div[1]'))).text
    #     driver.find_element_by_xpath('//*[@id="dl_cookieBanner"]/div/div/div/span/div[2]/button[1]').click()
    #     sleep(2)
    #     driver.find_element_by_xpath('//*[@id="dl_cookieBanner"]/div/div/div/span/div[2]/button[1]').click()
        
    # except:
    #     print('Nie przetlumaczono')
    # pl_biography = driver.find_element_by_css_selector('#target-dummydiv').text
    # print('Tutaj po polsku: \n', pl_biography)

    # CHUJ NIE ROBOTA Z TYMI TŁUMACZAMI

    # driver.get('https://translatica.pl/')

    # try:
    #     WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consent-modal-yr73k"]/div/div/div[4]/div/div[3]'))).click()
    #     sleep(2)
    #     WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consent-modal-yr73k"]/div/div/div[3]/div/div[3]'))).click()
    #     WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consent-modal-yr73k"]/div/div/div[3]/button[2]'))).click()
    #     WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consent-modal-yr73k"]/div/div/div[3]/button[1]'))).click()
    #     WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="consent-modal-yr73k"]/div/div/div[3]/button[1]'))).click()
    # except:
    #     print('Coś poszło nie tak przy sprzeciwie')

    # driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div[1]/div[1]/div[1]/section/div[1]/div[1]/div/div[1]/div[2]/button').click()

    # driver.find_element_by_xpath('//*[@id="source"]').send_keys(biography)
    # tlumacz = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div[1]/div[1]/div[1]/section/div[1]/div[2]/div/div[1]/div[2]/button')
    # tlumacz.click()
    # sleep(5)
    # pl_biography = driver.find_element_by_id('target').text
    # print('Tutaj po polsku: \n', pl_biography)

    translator = Translator()

    translated_bio = translator.translate(biography, dest='pl', src='en')
    pl_biography = translated_bio.text

    print('Tutaj po polsku: \n', pl_biography)
    personalia = biography.split(' ')[:3:]
    print(f'Imie: {personalia[0]} Drugie Imie: {personalia[1]} Nazwisko: {personalia[2]}')
    nowa_sciezka = './dane/'+personalia[2]+'_'+personalia[0]
    if not os.path.exists(nowa_sciezka):
        os.makedirs(nowa_sciezka)

    with open('dane/'+personalia[2]+'_'+personalia[0]+'/bio'+str(iterator)+'_'+personalia[2]+'_'+personalia[0]+'.txt', 'w') as f:
        f.write(biography)
        if isMale==False:
            f.write('\n\nFemale')
        else:
            f.write('\n\nMale')

    with open('dane/'+personalia[2]+'_'+personalia[0]+'/pl_bio'+str(iterator)+'_'+personalia[2]+'_'+personalia[0]+'.txt', 'w') as f:
        f.write(pl_biography)
        if isMale==False:
            f.write('\n\nKobieta')
        else:
            f.write('\n\nMężczyzna')

    with open('dane/'+personalia[2]+'_'+personalia[0]+'/pic'+str(iterator)+'_'+personalia[2]+'_'+personalia[0]+'.png', 'wb') as f:
        if isMale==False:
            f.write(female_grid[iterator])
        else:
            f.write(male_grid[iterator])

    driver.close()

def getPict(gender):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://generated.photos/faces/white-race/'+gender)

    sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/a[1]').click()
    driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div/main/div[2]/div/button/span').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div/main/div[2]/div/button/span').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div/main/div[2]/div/button/span').click()
    grid = [driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div/main/div[1]/div['+str(x)+']/a/img').screenshot_as_png for x in range(1, 101)]
    driver.close()

    return grid

male_grid = getPict('male')
female_grid = getPict('female')

for x in range(10):
    print(f'Getting #{x} Biography...')
    getBio(x)
    sleep(1)
    print(f'Biography #{x} got!')