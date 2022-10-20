package applications;

import base.BaseTest;
import login.LoginTest;
import org.testng.annotations.Test;
import pages.*;

public class SalesConsoleTest extends LoginTest {
    public SalesConsoleTest() throws Exception {
    }

    @Test()
    public void launchAccountsObject() throws Exception {
        // setupPage.clickOnAppLauncher();
        SalesConsolePage salesConsolePage = setupPage.clickOnSalesConsoleApp();
        Thread.sleep(5000);
        salesConsolePage.clickOnShowNavigationMenuButton();
        AccountsPage accountsPage = salesConsolePage.clickOnAccountsObject();
        accountsPage.clickOnNewButton();
        Thread.sleep(3000);
    }

    @Test
    public void launchOpportunitiesObject() throws Exception {
        SalesConsolePage salesConsolePage = setupPage.clickOnSalesConsoleApp();
        salesConsolePage.clickOnShowNavigationMenuButton();
        //Thread.sleep(3000);
        OpportunityPage opportunityPage = salesConsolePage.clickOnOpportunityObject();
        opportunityPage.clickOnNewButtonOnOpp();
        Thread.sleep(3000);
    }

    @Test(groups = "contact_creation")
    public void launchContactsObject() throws Exception{
        SalesConsolePage salesConsolePage = setupPage.clickOnSalesConsoleApp();
        salesConsolePage.clickOnShowNavigationMenuButton();
        Thread.sleep(3000);
        ContactsPage contactsPage = salesConsolePage.clickOnContactObject();
        contactsPage.clickOnNewButtonOnContacts();
        Thread.sleep(3000);
    }
}
