import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;
import org.testng.annotations.AfterClass;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.android.AndroidDriver;
import java.net.URL;
import org.openqa.selenium.remote.CapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;

public class Driver{

    public AppiumDriver driver;

    @Before
    public void setUp(){
    DesiredCapabilities dc = new DesiredCapabilities();
    dc.setCapability("platformName","Android");
    dc.setCapability("deviceName", "emulator-5554");
    dc.setCapability("platformVersion", "9");
    dc.setCapability("appPackage","tv.tolka.vhometv");
    dc.setCapability("appWaitActivity","com.tolka.woctv.activity.s");
    dc.setCapability("sessionOverride",true);
    driver = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"),dc);




}

    @Test
    public void testplus() {
    
        driver.findElementById("tv.tolka.vhometv:id/btn_one").click();
        
    }
    @AfterClass
    public void tearDown() 
    {
        driver.quit();
    }



}