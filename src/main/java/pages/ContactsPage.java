package pages;

import org.openqa.selenium.*;
import org.openqa.selenium.interactions.Actions;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;

public class ContactsPage {
    private WebDriver driver;
    private By newButtonOnContacts = By.xpath("//div[@title = 'New']");
    private By firstNameField = By.xpath("//input[@name = 'firstName']");
    private By lastNameField = By.xpath("//input[@name = 'lastName']");
    private By phoneField = By.xpath("//input[@name = 'Phone']");
    private By accountLookup = By.xpath("//input[@placeholder= 'Search Accounts...']");
    private By selectAccount = By.xpath("//ul[@role='group']//lightning-base-combobox-item[@data-value='0012w00001359gKAAQ']");
    private By birthdateField = By.xpath("//input[@name= 'Birthdate']");
    private By birthdateCalendar = By.xpath("//button[@title='Select a date for Birthdate']");
    private By saveButton = By.xpath("//button[@name='SaveEdit']");
    private By birthdayToday = By.xpath("//div[text(), 'Today']");

    public ContactsPage(WebDriver driver) {
        this.driver = driver;
    }

    public void clickOnNewButtonOnContacts() {
        driver.findElement(newButtonOnContacts).click();
    }

    public ContactRecordPage createNewContact() throws Exception {
        DateFormat dateFormat = new SimpleDateFormat("MM/dd/yyyy");
        Date date = new Date();
        String date1 = dateFormat.format(date);
        driver.findElement(firstNameField).sendKeys("Automated");
        driver.findElement(lastNameField).sendKeys("Contact"+System.currentTimeMillis());
        //driver.findElement(phoneField).sendKeys("9988776655");
        driver.findElement(accountLookup).click();
        Thread.sleep(3000);
        driver.findElement(selectAccount).click();
        driver.findElement(birthdateField).sendKeys("12/09/1992");
        Thread.sleep(3000);
        driver.findElement(saveButton).click();
        return new ContactRecordPage(driver);
    }
}
