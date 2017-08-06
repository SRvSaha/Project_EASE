import edu.stanford.nlp.tagger.maxent.MaxentTagger;
import java.io.*;
import java.util.LinkedHashSet;

public class POSTagging {

	/**
	 * @param args
	 * @throws Exception 
	 */
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
//		MaxentTagger tagger = new MaxentTagger("/home/srvsaha/Project_EASE/stanford-postagger-full-2017-06-09/models/wsj-0-18-bidirectional-distsim.tagger");
		MaxentTagger tagger = new MaxentTagger("/home/srvsaha/Project_EASE/stanford-postagger-full-2017-06-09/models/english-left3words-distsim.tagger");
		BufferedReader br = new BufferedReader(new FileReader("/home/srvsaha/Project_EASE/Data/test_dataset.txt"));
		BufferedWriter bw = new BufferedWriter(new FileWriter("/home/srvsaha/Project_EASE/Data/stanford_pos_extracted_keywords.txt"));
		LinkedHashSet<String> outputSet = new LinkedHashSet<String>();
		try
		{
			String line = br.readLine();
			String tagged, output = "";
			String[] recipes, instructions, tagged_words, tokens;
			while(line != null)
			{
				
				recipes = line.split("\t");
				if (recipes.length == 3)
				{	
					output = recipes[0]+"\n";
					bw.write(output);
					int len = Integer.parseInt(recipes[2]);
					while(len > 0)
					{
						output = "";
						line = br.readLine();
						instructions = line.split("\t");
						tagged = tagger.tagString(instructions[1]);
						tagged_words = tagged.split(" ");
						for(String w:tagged_words)
						{
							tokens = w.split("_");
							if((tokens[1].toString().startsWith("N") || tokens[1].toString().startsWith("V")) && !((tokens[0].toString().equals("°C")) || (tokens[0].toString().equals("°F"))))
							{
								outputSet.add(tokens[0].toLowerCase());
							}
						}
						for(String x: outputSet)
						{
							output += x + '\t';
						}
						output = output.trim();
//						System.out.print(output);
						bw.write(instructions[0] + '\t' + output + '\n');
						output = "";
						outputSet.clear();
						len -= 1;
//						System.out.println();
					}
				}
//				System.out.println();
				line = br.readLine();
			}
		}finally{
			br.close();
			bw.close();
			System.out.println("Output Successful");
		}
			
	}

}
