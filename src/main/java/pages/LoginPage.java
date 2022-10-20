package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Properties;


public class LoginPage {
    private WebDriver driver;
    private By usernameField = By.xpath("//input[@id='username']");
    private By passwordField = By.xpath("//input[@id='password']");
    private By loginButton = By.xpath("//input[@id='Login']");
    private By rememberMeCheckbox = By.xpath("//input[@id='rememberUn']");
    private By forgotPasswordLink = By.xpath("//a[@id='forgot_password_link']");


    //constructor
    public LoginPage(WebDriver driver) throws Exception {
        this.driver = driver;
    }

    public void setUsername(String username) {
        driver.findElement(usernameField).sendKeys(username);
    }

    public void setPassword(String password){
        driver.findElement(passwordField).sendKeys(password);
    }

    public SetupPage clickOnLoginButton() {
        driver.findElement(loginButton).click();
        return new SetupPage(driver);
    }
}
