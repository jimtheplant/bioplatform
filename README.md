# BioPlatform

Biological data, done right.

## Description

For decades the bioinformatic's community has lagged behind in creating common interfaces for our data, while 
advances in data science and software engineering have made this easier than ever. 
Unfortunately, it is rare that experts in biology have the software engineering knowledge and time to use these new tools. 
The result is hundreds of niche data sources and formats that are incompatible or dated. 
<br/>
The Graph Query Language (GraphQL) is an elegant solution to this issue. Originally designed by Facebook as a user centric 
query interface, it has seen widespread adoption by organizations such as GitHub, IBM, Twitter, and Walmart. GraphQL allows for 
API's that are highly structured, yet flexible for users. Essentially, developers are able to use whatever technologies necessary 
to create their API schemas, and API consumers are able to query in a more natural way. See [the GraphQL](https://graphql.org/learn/) 
introduction to learn more.
<br/>
This project aims to provide a framework for the modularization of biological data to ease in the sharing and development
of new tools. This core package, will let users inject their own modules to a base schema, give several pre-built query types, 
and have basic data provenance capabilities. 

## Getting Started

### Dependencies

* [Python 3.7+](https://www.python.org/downloads/release/python-370/)
* [graphene](https://graphene-python.org/)
* [uvicorn](https://www.uvicorn.org/)

### Installing
BioPlatform uses [pip]() for installation. To install, run 

```
pip install bio-platform
``` 

### Executing program
To start the server, import univorn, pass an initializer to the app factory method, and run the app.
```
import uvicorn

initializer = CustomInitializer()
app = app_factory([initializer])

uvicorn.start(app)
```
## Best Practices
### Core Ideas
Bio-platform has a set of common philosophies for module development. This will ensure modules can be reused 
and modified by others. In extreme cases these philosophies can be bended, but 
following these best practices ensure a pluggable architecture for your project.
1. **One module, one initializer one base query type.**
    1. An initializer is the object that should bootstrap the whole module. Only one should be passed to the app 
    factory and it's init method should only return the base query for the module.
    2. This goes along with GraphQL's idea of only querying the data that is needed. Think of the business domain that 
    your module is trying to solve. For hints see the [GraphQL best practice guide](https://graphql.org/learn/best-practices/).
## Help

Feel free to post issues here on GitHub. This is a very young project, so there's bound to be bugs and questions that arise.
We are always looking for help so if you want to contribute, post a pull request. Sometimes I will stream my development
on [Twitch](https://www.twitch.tv/jimtheplant), bring questions and maybe I can help out.

## Authors

* Jim the Plant 
    * [Twitter](https://twitter.com/jimtheplant1)
    * [Twitch](https://www.twitch.tv/jimtheplant)
    * jimtheplant1@gmail.com
    

## Version History

* 0.0.1
    * Initial Release

## License

This project is licensed under the Apache 2.0 License - see the LICENSE file for details
