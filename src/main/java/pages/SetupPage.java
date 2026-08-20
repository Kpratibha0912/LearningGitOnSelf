package pages;

import org.omg.IOP.TAG_JAVA_CODEBASE;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class SetupPage{
    private WebDriver driver;
    private By appLauncher = By.xpath("//div[@class='slds-icon-waffle']");
    private By salesConsoleApp = By.xpath("//p[contains(text(), 'Sales Console')]");

    public SetupPage(WebDriver driver) {
        this.driver = driver;
    }

    public void clickOnAppLauncher() {
        driver.findElement(appLauncher).click();
    }

    public SalesConsolePage clickOnSalesConsoleApp() {
        driver.findElement(salesConsoleApp).click();
        return new SalesConsolePage(driver);
    }
}
