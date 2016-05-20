/**
 * Created by anjieliang on 5/19/16.
 */
import java.util.*;
import java.io.*;

public class NLG {
    private HashMap<String, HashMap<String, Double>> primary;

    public NLG(String fileName) throws Exception {
        //set up a reader for the csv
        FileReader fr = null;
        try {
            fr = new FileReader(fileName);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        BufferedReader reader = new BufferedReader(fr);
        //set up data structure
        primary = new HashMap<String, HashMap<String, Double>>();
        String[] tickers = reader.readLine().split(",");

        for(int i = 1; i < tickers.length; i++) {
            primary.put(tickers[i], new HashMap<String, Double>());
        }

        String line;
        while((line = reader.readLine()) != null) {
            String[] values = line.split(",");
            for(int i = 1; i < values.length; i++) {
                Double insert;
                if(values[i].equals("")) {
                    insert = null;
                }
                else {
                    insert = Double.parseDouble(values[i]);
                }
                primary.get(tickers[i]).put(values[0], insert);
            }
        }
    }

    public HashMap<String, HashMap<String, Double>> getPrimary() {
        return primary;
    }

    public Double getValue(String ticker, String date) {
        return primary.get(ticker).get(date);
    }

    public Double getDelta(String ticker, String date1, String date2) {
        return primary.get(ticker).get(date2) - primary.get(ticker).get(date1);
    }

    public static void main(String[] args) throws Exception {
        NLG generator = new NLG("test.txt");
        Scanner readIn = new Scanner(System.in);
        while(readIn.hasNext()) {
            String[] query = readIn.nextLine().split(" ");
            if(query.length == 2) {
                System.out.println(generator.getValue(query[0], query[1]));
            }
            else if(query.length == 3) {
                System.out.println(generator.getDelta(query[0], query[1], query[2]));
            }
        }
    }

}
