CREATE TABLE IF NOT EXISTS PROPERTY (
    property_id INT AUTO_INCREMENT PRIMARY KEY,
	School_Average      DOUBLE,
	Latitude      DOUBLE,
	Longitude           DOUBLE,
	Subdivision        varchar(20),
	Rent_Restricted     varchar(20),
	Neighborhood_Rating   int,
	Flood     varchar(20),
	Street_Address     varchar(50),
	City       varchar(50),
	State   varchar(20),
	Zip     int,
	Property_Type  varchar(20),
	Highway       varchar(20), 
	Train         varchar(20),
	Tax_Rate      DOUBLE,
	SQFT_Basement   int,
	HTW           varchar(20),
	Pool      varchar(20),
	Commercial    varchar(20),
	Water           varchar(20),
	Sewage         varchar(20), 
	Year_Built      int, 
	SQFT_MU      int,
	SQFT_Total     varchar(20),
	Parking       varchar(20), 
	Bed            varchar(20),
	Bath            int,
	BasementYesNo   varchar(20),
	Layout               varchar(20),
	Market                varchar(20),
	Property_Title       varchar(100),
	Address            varchar(100)

)ENGINE=InnoDB;


CREATE TABLE IF NOT EXISTS LEADS (
  leads_id INT AUTO_INCREMENT PRIMARY KEY,
  property_id      INT, 
  Reviewed_Status     varchar(20),
Most_Recent_Status    varchar(20),
Source                varchar(20),
Occupancy              varchar(10),
Net_Yield               DOUBLE,
IRR                      DOUBLE,
Selling_Reason            varchar(20),
Seller_Retained_Broker      varchar(20),
Final_Reviewer               varchar(50),

FOREIGN KEY (property_id) REFERENCES PROPERTY(property_id)
)ENGINE=InnoDB;


CREATE TABLE IF NOT EXISTS HOA (
  hoa_id INT AUTO_INCREMENT PRIMARY KEY,
  property_id    INT,
  HOA_Flag         varchar(10),
  HOA int,

FOREIGN KEY (property_id) REFERENCES PROPERTY(property_id)  

) ENGINE=InnoDB;


CREATE TABLE IF NOT EXISTS VALUATION (
valuation_id INT AUTO_INCREMENT PRIMARY KEY,
property_id     int,
Previous_Rent      DOUBLE,
List_Price         DOUBLE,
Zestimate          DOUBLE,
ARV                DOUBLE,
Expected_Rent      DOUBLE,
Rent_Zestimate     DOUBLE,
Low_FMR            DOUBLE,
High_FMR           DOUBLE,
Redfin_Value       DOUBLE,

FOREIGN KEY (property_id) REFERENCES PROPERTY(property_id)    
) ENGINE=InnoDB;


CREATE TABLE IF NOT EXISTS TAXES (
 tax_id INT AUTO_INCREMENT PRIMARY KEY,
 property_id   int,
  Taxes         int,
FOREIGN KEY (property_id) REFERENCES PROPERTY(property_id)  

) ENGINE=InnoDB;



CREATE TABLE IF NOT EXISTS REHAB (
rehab_id INT AUTO_INCREMENT PRIMARY KEY,
property_id          int,
Underwriting_Rehab	 int,
Rehab_Calculation	 int, 
Paint	             varchar (20),
Flooring_Flag	     varchar (20),
Foundation_Flag	     varchar (20),
Roof_Flag	         varchar (20),
HVAC_Flag	         varchar (20),
Kitchen_Flag	     varchar (20),
Bathroom_Flag	     varchar (20), 
Appliances_Flag	     varchar (20),
Windows_Flag	     varchar (20),
Landscaping_Flag	 varchar (20),
Trashout_Flag	     varchar (20),
FOREIGN KEY (property_id) REFERENCES PROPERTY(property_id) 

)ENGINE=InnoDB;

