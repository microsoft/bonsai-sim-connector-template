# IMPORTANT: **docs-snippets branch**

> This docs-snippets branch of the connector template is used by the [Bonsai Connectors documentation](https://docs.microsoft.com/en-us/autonomous-systems/bonsai-connectors/).
> Documentation pulls code snippets from the template using [Named snippets](https://docs.microsoft.com/en-us/contribute/code-in-docs#named-snippet).
> We don't want the main branch to contain these snippets because:
>
> 1. They are unnecessary for users of the template, who could be confused by the extra snippet comments.
> 2. Changes could be made to the template without awareness of how the doc snippets are used, leaving
> 3. the docs with broken snippets or mismatched information.
>
> By using this branch, the snippets are frozen in time. When we do want to update the docs with an updated
> version of the connector code, the main branch can be merged into the docs-snippets branch.

# About bonsai-sim-connector-template

This is a template for creating [Bonsai Connectors](https://docs.microsoft.com/en-us/autonomous-systems/bonsai-connectors). It can serve
as a starting point for making a simulation platform work with Bonsai.

> Note that this template assumes you will be developing in Python. Bonsai also supports
> [Java and TypeScript libraries](https://github.com/microsoft/microsoft-bonsai-api). For those languages, you *can* use this template,
> but you will need to adjust the Python portions to perform the equivalent operations in the other language.

You can use this template by:
1. Use GitHub to [create a new repository based on this template](https://github.com/microsoft/bonsai-sim-connector-template/generate). Or
if you don't prefer to use GitHub you make a copy of the files however you like.
2. Find and replace SIM_PLATFORM with the name of the simulation platform for which you are making a connector.
3. Find and replace SAMPLE_NAME with the name of a sample use case that you will use to demonstrate your connector.
4. Find the sections of the connector that say "TODO" and implement the required functionality. See
[Build a Python connector](https://docs.microsoft.com/en-us/autonomous-systems/bonsai-connectors/guides/dedicated-connector-python) for more
information about Bonsai connectors and step-by-step instructions for implementing one.
5. Delete these instructions. Your users are interested in your connector--not the template that it came from. Remove this whole section from this point to the top of the file.

# SIM_PLATFORM connector

A connector for using SIM_PLATFORM with [Microsoft Project Bonsai](https://azure.microsoft.com/en-us/services/project-bonsai/).

> TODO: Give a brief overview of the capabilities of SIM_PLATFORM and entice users with potential use cases for using SIM_PLATFORM to create Bonsai brains for controlling autonomous systems.

## Samples

[SAMPLE_NAME](samples/SAMPLE_NAME/README.md)

> TODO: Describe how a user could customize the supplied sample to run a different simulation model that they created with SIM_PLATFORM.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
