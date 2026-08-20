package login;

import base.BaseTest;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
import pages.SetupPage;

public class LoginTest extends BaseTest {
    public LoginTest() throws Exception {
    }

    @BeforeMethod
    @Test
    public void loginToSalesforce() throws Exception {

        loginPage.setUsername("pratibha@myorg.com");
        loginPage.setPassword("Pratz@0912");
        SetupPage setupPage = loginPage.clickOnLoginButton();
        setupPage.clickOnAppLauncher();

    }
}
