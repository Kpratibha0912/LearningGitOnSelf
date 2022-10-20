package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class OpportunityPage {
    private WebDriver driver;
    private By newButtonOnOpp = By.xpath("//div[@title= 'New']");

    public OpportunityPage(WebDriver driver){
        this.driver=driver;
    }

    public void clickOnNewButtonOnOpp(){
        driver.findElement(newButtonOnOpp).click();
    }
}
