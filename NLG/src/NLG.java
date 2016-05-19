/**
 * Created by anjieliang on 5/19/16.
 */
public class NLG {
    BufferedReader reader;

    public static void main(String[] args) {
        reader = new getReader("input.csv");
    }

    private static BufferedReader getReader(String fileName) {
        info = new HashMap<String, StockInfo>();
        FileReader fr = null;
        try {
            fr = new FileReader(fileName);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return new BufferedReader(fr);
    }

    private static HashMap<String, HashMap<String, String>> setHashmaps() {
        HashMap<String, HashMap<String, String>> primary = new HashMap<String, HashMap<String, String>>();
    }



    /*
        public void outputResult(String fileName) {
        FileWriter output = null;
        try {
            output = new FileWriter(fileName);
            BufferedWriter writer = new BufferedWriter(output);

            String[] arr = new String[4];
            String cur = reader.readLine();
            while(cur != null) {
                arr = cur.split(",");
                if(info.containsKey(arr[1])) {
                    info.get(arr[1]).addEntry(Long.parseLong(arr[0]),Integer.parseInt(arr[2]),Integer.parseInt(arr[3]));
                }
                else {
                    info.put(arr[1], new StockInfo(Long.parseLong(arr[0]),Integer.parseInt(arr[2]),Integer.parseInt(arr[3])));
                }
                cur = reader.readLine();
            }

            TreeMap<String, StockInfo> sorted = new TreeMap<String, StockInfo>(info);
            Set<Map.Entry<String, StockInfo>> entries = sorted.entrySet();
            Iterator<Map.Entry<String, StockInfo>> iter = entries.iterator();
            while(iter.hasNext()) {
                Map.Entry<String, StockInfo> entry = iter.next();
                writer.write(entry.getKey() + "," + entry.getValue().toString());
                writer.newLine();
            }

            reader.close();
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
     */
}
