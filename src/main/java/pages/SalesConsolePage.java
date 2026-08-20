package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;

import java.util.List;

public class SalesConsolePage {
    private WebDriver driver;
    private By showNavigationMenuButton = By.xpath("//button[@title = 'Show Navigation Menu']");
    private By accountsOption = By.xpath("//span[contains(text(), 'Accounts')]");
    private By opportunityOption  = By.xpath("//span[contains(text(), 'Opportunities')]");
    private By contactOption = By.xpath("//span[contains(text(), 'Contacts')]");


    public SalesConsolePage(WebDriver driver) {
        this.driver = driver;
    }

    public void clickOnShowNavigationMenuButton() throws Exception {
        driver.findElement(showNavigationMenuButton).click();
        Thread.sleep(2000);
    }

    public AccountsPage clickOnAccountsObject() throws Exception {
        JavascriptExecutor jse = (JavascriptExecutor) driver;
        jse.executeScript("arguments[0].scrollIntoView", driver.findElement(accountsOption) );
        Thread.sleep(3000);
        Actions actions = new Actions(driver);
        actions.moveToElement(driver.findElement(accountsOption)).click().build().perform();
        Thread.sleep(3000);
        return new AccountsPage(driver);
    }

    public OpportunityPage clickOnOpportunityObject() throws Exception{
        JavascriptExecutor jse = (JavascriptExecutor) driver;
        jse.executeScript("arguments[0].scrollIntoView", driver.findElement(opportunityOption));
        Thread.sleep(3000);
        Actions actions = new Actions(driver);
        actions.moveToElement(driver.findElement(opportunityOption)).click().build().perform();
        Thread.sleep(3000);
        return new OpportunityPage(driver);
    }

    public ContactsPage clickOnContactObject() throws Exception {
        JavascriptExecutor jse = (JavascriptExecutor) driver;
        jse.executeScript("arguments[0].scrollIntoView", driver.findElement(contactOption));
        Thread.sleep(3000);
        Actions actions = new Actions(driver);
        actions.moveToElement(driver.findElement(contactOption)).click().build().perform();
        return new ContactsPage(driver);
    }
}
