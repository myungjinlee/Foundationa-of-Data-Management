import java.io.IOException;
import java.util.StringTokenizer;
import java.text.NumberFormat;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;


public class BusyMonth {

  public static class TokenizerMapper 
       extends Mapper<Object, Text, Text, IntWritable>{
    
    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();
    
    public void map(Object key, Text value, Context context
                    ) throws IOException, InterruptedException {
      String myvalue = new String(); 
      String [] listString = value.toString().split(",");
      if (listString[2].equals("Terminal 1") || listString[2].equals("Terminal 2") 
          || listString[2].equals("Terminal 3") || listString[2].equals("Terminal 4") 
          ||listString[2].equals("Terminal 5") || listString[2].equals("Terminal 6") 
          || listString[2].equals("Terminal 7") || listString[2].equals("Terminal 8") 
          || listString[2].equals("Tom Bradley International Terminal") ){
         
        String first  = value.toString().substring(23,26);
        String second = value.toString().substring(29,33);
        myvalue = first + "" + second;
      
      StringTokenizer itr = new StringTokenizer(myvalue.toString());
      IntWritable number = new IntWritable(Integer.parseInt(listString[5])); 
        while (itr.hasMoreTokens()) {
        word.set(itr.nextToken());
        context.write(word, number);
      }
    } 
    }
  }
  
  public static class IntSumReducer 
       extends Reducer<Text,IntWritable,Text,IntWritable> {
    private IntWritable result = new IntWritable(1);
    public void reduce(Text key, Iterable<IntWritable> values, 
                       Context context
                       ) throws IOException, InterruptedException {
      int sum = 0;
      for (IntWritable val : values) {
        sum += val.get();
      }
      //result.set(sum);
      if (sum > 5000000) {
      result.set(sum);
      context.write(key, result);
     }
    }
  }

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
    if (otherArgs.length < 2) {
      System.err.println("Usage: wordcount <in> [<in>...] <out>");
      System.exit(2);
    }
    Job job = Job.getInstance(conf, "word count");
    job.setJarByClass(BusyMonth.class);
    job.setMapperClass(TokenizerMapper.class);
    job.setCombinerClass(IntSumReducer.class);
    job.setReducerClass(IntSumReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
    for (int i = 0; i < otherArgs.length - 1; ++i) {
      FileInputFormat.addInputPath(job, new Path(otherArgs[i]));
    }
    FileOutputFormat.setOutputPath(job,
      new Path(otherArgs[otherArgs.length - 1]));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
