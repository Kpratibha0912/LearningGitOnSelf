package applications;

import login.LoginTest;
import org.openqa.selenium.WebDriver;
import org.testng.annotations.Test;
import pages.ContactRecordPage;
import pages.ContactsPage;
import pages.SalesConsolePage;

public class ContactsTest extends SalesConsoleTest {

    public ContactsTest() throws Exception {
    }

    WebDriver driver;

    @Test
    public void createNewContactTest() throws Exception {
        salesConsolePage = setupPage.clickOnSalesConsoleApp();
        salesConsolePage.clickOnShowNavigationMenuButton();
        ContactsPage contactsPage = salesConsolePage.clickOnContactObject();
        contactsPage.clickOnNewButtonOnContacts();
        ContactRecordPage contactRecordPage = contactsPage.createNewContact();
        Thread.sleep(3000);
        contactRecordPage.clickOnDetailsTab();
    }

}
