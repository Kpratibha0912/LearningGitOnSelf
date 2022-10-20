package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class AccountsPage {
    public WebDriver driver;
    private By accountIcon = By.xpath("//div[@class='slds-grid']//img");
    private By newButtonOnAccounts = By.xpath("//div[@title = 'New']");


    public AccountsPage(WebDriver driver){
        this.driver = driver;
    }

    public void clickOnNewButton(){
        driver.findElement(newButtonOnAccounts).click();
    }

    public void createNewAccount(){

    }
}
