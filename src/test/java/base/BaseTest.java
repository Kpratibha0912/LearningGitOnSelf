package base;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeTest;
import pages.*;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Properties;
import java.util.concurrent.TimeUnit;

public class BaseTest {
    private WebDriver driver;
    protected LoginPage loginPage;
    protected SetupPage setupPage;
    protected SalesConsolePage salesConsolePage;
    protected AccountsPage accountsPage;
    protected OpportunityPage opportunityPage;
    protected ContactsPage contactsPage;

    @BeforeClass
    public void setUp() throws Exception {
        System.setProperty("webdriver.chrome.driver", "resources//chromedriver.exe");
        driver = new ChromeDriver();
        driver.manage().deleteAllCookies();
        driver.manage().window().maximize();
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);

        driver.get("http://login.salesforce.com");
        loginPage = new LoginPage(driver);
        setupPage = new SetupPage(driver);
        salesConsolePage = new SalesConsolePage(driver);
        accountsPage = new AccountsPage(driver);
        opportunityPage = new OpportunityPage(driver);

    }

    @AfterClass
    public void browserTearDown(){
        driver.quit();
    }
}
