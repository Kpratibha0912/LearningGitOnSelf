package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.interactions.Actions;

public class ContactRecordPage {
    private WebDriver driver;
    private By goToDetailsTab = By.xpath("//flexipage-component2[@data-component-id='flexipage_tabset']//ul//li[@title='Details']");
    private By recordName = By.xpath("//slot[@name ='primaryField']//span[contains(text(), 'manual created')]");

    public ContactRecordPage(WebDriver driver){
        this.driver = driver;
    }

    public void verifyTitleOfContact(){

    }

    public void clickOnDetailsTab(){
        JavascriptExecutor jse = (JavascriptExecutor) driver;
        jse.executeScript("arguments[0].scrollIntoView", driver.findElement(goToDetailsTab));
        Actions actions = new Actions(driver);
        actions.moveToElement(driver.findElement(goToDetailsTab)).click().build().perform();
    }
}
