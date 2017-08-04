/*
#
#   @author      : SRvSaha
#   Filename     : Lemmatization.java
#   Timestamp    : 10:12 04-August-2017 (Friday)
#   Description  : Lemmatization using Stanford Lemmatizer
#
*/

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.LinkedList;
import java.util.List;
import java.util.Properties;

import edu.stanford.nlp.ling.CoreAnnotations.LemmaAnnotation;
import edu.stanford.nlp.ling.CoreAnnotations.SentencesAnnotation;
import edu.stanford.nlp.ling.CoreAnnotations.TokensAnnotation;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.pipeline.Annotation;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;
import edu.stanford.nlp.util.CoreMap;

public class Lemmatization {

    protected StanfordCoreNLP pipeline;

    public Lemmatization() {
        // Create StanfordCoreNLP object properties, with POS tagging
        // (required for lemmatization), and lemmatization
        Properties props;
        props = new Properties();
        props.put("annotators", "tokenize, ssplit, pos, lemma");
        /*
         * This is a pipeline that takes in a string and returns various analyzed linguistic forms.
         * The String is tokenized via a tokenizer (such as PTBTokenizerAnnotator),
         * and then other sequence model style annotation can be used to add things like lemmas,
         * POS tags, and named entities. These are returned as a list of CoreLabels.
         * Other analysis components build and store parse trees, dependency graphs, etc.
         *
         * This class is designed to apply multiple Annotators to an Annotation.
         * The idea is that you first build up the pipeline by adding Annotators,
         * and then you take the objects you wish to annotate and pass them in and
         * get in return a fully annotated object.
         *
         *  StanfordCoreNLP loads a lot of models, so you probably
         *  only want to do this once per execution
         */
        this.pipeline = new StanfordCoreNLP(props);
    }

    public List<String> lemmatize(String documentText)
    {
        List<String> lemmas = new LinkedList<String>();
        // Create an empty Annotation just with the given text
        Annotation document = new Annotation(documentText);
        // run all Annotators on this text
        this.pipeline.annotate(document);
        // Iterate over all of the sentences found
        List<CoreMap> sentences = document.get(SentencesAnnotation.class);
        for(CoreMap sentence: sentences) {
            // Iterate over all tokens in a sentence
            for (CoreLabel token: sentence.get(TokensAnnotation.class)) {
                // Retrieve and add the lemma for each word into the
                // list of lemmas
                lemmas.add(token.get(LemmaAnnotation.class));
            }
        }
        return lemmas;
    }


    public static void main(String[] args) throws IOException {
        System.out.println("Starting Stanford Lemmatizer");
        Lemmatization stanfordLemma = new Lemmatization();
        BufferedReader br = new BufferedReader(new FileReader("/home/srvsaha/Project_EASE/Data/stanford_pos_extracted_keywords.txt"));
        BufferedWriter bw = new BufferedWriter(new FileWriter("/home/srvsaha/Project_EASE/Data/stanford_lemmatized_extracted_keywords.txt"));
        String line = br.readLine();
        String output, marker;
        while(line != null)
        {
        	output = "";
        	if(line.startsWith("R"))
        	{
        		bw.write(line);
        		bw.newLine();
        	}
        	else
        	{
        		marker = line.substring(0, line.indexOf("\t")+1);
        		line = line.substring(line.indexOf("\t")+1);
        		for(String keyword : stanfordLemma.lemmatize(line))
        		{
        			output += keyword + '\t';
        		}
        		bw.write(marker + output.trim() + '\n');
        	}
        	line = br.readLine();
        }
        br.close();
        bw.close();
        System.out.println("Output Successful");
    }

}