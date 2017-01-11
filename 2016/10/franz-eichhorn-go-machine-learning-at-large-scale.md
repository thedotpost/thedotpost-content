Conference: dotgo-2016
Tags: Golang
Filmed: 2016-10-10
Author: franzeichhorn
Image: https://farm6.staticflickr.com/5727/30277372295_7ce3af8c0e_k_d.jpg
Title: Go machine learning at large scale
Curator: sylvinus
Category: Backend
Summary: Go can be used to execute machine learning models in live production systems. Franz points out challenges when training models in Go and why you should consider using other technologies.
Slides: https://speakerdeck.com/player/8266439d129a4e26a2ac208f886ec0ed
Video: https://www.youtube.com/watch?v=_RQmCUk3SGY
Template: talk
Date: 2017-01-11 12:27:33


### Transcript:

On our social platform there are more than 50 million users, which produce by interacting with each other roughly 1 million requests per minute. We're using machine learning to make different decisions, for example finding possible chat partners or separating the good guys from the bad guys by filtering spam. To accomplish that we're using Go because it allows us to easily build high-performant concurrent systems that are able to cope with this amount of data.

To use models, we need to train them first and for that we're using historical data stored in hadoop. Since we are using Go at runtime, it would also be nice to use Go for the training. But there are some problems: First, it's impossible to download the data from hadoop, so we need to move the model training, which complicates deployment and debugging. Second, when working with machine learning, most of the time is spent on feature extraction as well as preprocessing, cleaning and sampling the data instead of doing the actual model training. While doing that in go is possible, it is very convenient because this is simply not what Go was created for.

Instead we want to use dedicated tools like Spark and R as well as visual tools like Knime or RapidMiner which perform all these steps of model training perfectly integrated with hadoop. This approach has two more advantages: It simplifies our runtime libraries and second, more importantly, allows the data scientists to do their work with the technologies they know and like.

Now we have perfect models; but executing them in Spark or R brings a new set a of problems, that's why we would like to run them in Go again, so let's talk about how to accomplish that.
A trained model is basically a bunch of numbers and conditions, and implementing these in Go is pretty easy. Two examples:

Take a random forest with 100 trees: exporting that to a markup language creates a file of roughly 90MB in size. Our first approach was to generate the model as pure Go code. That is easy, as a random forest consists of decision trees which can directly be expressed as conditional statements in Go. The resulting code however is roughly 40MB, and compiling that makes your computer stuck for 20 minutes and you are lucky if it ever stops swapping.
That’s why we went to generating code that just loads and interprets the model at runtime having similar execution speed but without the compiler hassle.

The second example is a logistic regression model where it is even easier, since we can simply export the model coefficients to Json and generate code that performs the computation at runtime.

These examples may look like custom solutions, but the idea of executing a trained model using generated code can actually be applied to many different models once you know the particular format. And that has proven to be very successful for our purposes.

Plus, it avoids using a full-blown machine learning library in Go and uses Go where it really shines.

Thanks!