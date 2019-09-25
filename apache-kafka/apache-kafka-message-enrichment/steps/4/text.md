
2 actionable tasks: 2 executed
To download a copy of the MaxMind GeoIP free database, execute this command:

Copy
$ wget "http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz"
Run the following command to decompress the file:

Copy
$ gunzip GeoLiteCity.dat.gz
Move the GeoLiteCity.dat file in a route accessible to our program.

Now, add a file called GeoIPService.java in the src/main/java/monedero/extractors directory containing the content of Listing 3.2:

Copy
package monedero.extractors;
import com.maxmind.geoip.Location;
import com.maxmind.geoip.LookupService;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
public final class GeoIPService {
  private static final String MAXMINDDB = "/path_to_your_GeoLiteCity.dat_file";
  public Location getLocation(String ipAddress) {
    try {
      final LookupService maxmind = 
        new LookupService(MAXMINDDB, LookupService.GEOIP_MEMORY_CACHE);
      return maxmind.getLocation(ipAddress);
    } catch (IOException ex) {
      Logger.getLogger(GeoIPService.class.getName()).log(Level.SEVERE, null, ex);
    }
    return null;
  }
}
Listing 3.2: GeoIPService.java

The GeoIPService has a public method getLocation that receives a string representing the IP address and looks for this IP address in the GeoIP location database. This method returns an object of class location with the geographic location of that specific IP address.