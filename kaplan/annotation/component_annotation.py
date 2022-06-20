import rdflib
from rdflib import XSD, RDFS

from kaplan.annotation.decorator import component
from kaplan.annotation.ontology import ontology

BIGOWL = ontology(uri="http://www.ontologies.khaos.uma.es/bigowl/")
RDF = ontology(uri="http://www.w3.org/1999/02/22-rdf-syntax-ns#")
TITAN = ontology(uri="http://www.ontologies.khaos.uma.es/titan-kaplan/")

SelectionComponent = component(TITAN.uri, {"hasParameter": BIGOWL.namespace.hasParameter,
                                           "hasParameterType": BIGOWL.namespace.hasParameter,
                                           "hasParameterSolution": BIGOWL.namespace.hasParameter,
                                           "hasParameterMating": BIGOWL.namespace.hasParameter,
                                           "hasImplementation": BIGOWL.namespace.hasImplementation,
                                           "specifiesOutputClass": BIGOWL.namespace.specifiesOutputClass,
                                           "specifiesInputClass": BIGOWL.namespace.specifiesInputClass,
                                           "hasSolution": BIGOWL.namespace.hasSolutionComponent,
                                           "type": RDF.namespace.type,
                                           "label": RDFS.label},
                              {"hasParameter": TITAN.namespace.parameter_operator_name,
                               "hasParameterType": TITAN.namespace.parameter_selection_type,
                               "hasParameterSolution": TITAN.namespace.parameter_solution_type,
                               "hasParameterMating": TITAN.namespace.parameter_mating_pool_size,
                               "hasImplementation": TITAN.namespace.ImplementationSelection,
                               "specifiesOutputClass": TITAN.namespace.DataSelection,
                               "specifiesInputClass": TITAN.namespace.DataTermination,
                               "hasSolution": BIGOWL.namespace.GenericSolution,
                               "type": BIGOWL.namespace.Selection,
                               "label": rdflib.Literal('Selection', datatype=XSD.string)})

EvaluationComponent = component(TITAN.uri, {"hasParameter": BIGOWL.namespace.hasParameter,
                                           "hasParameterType": BIGOWL.namespace.hasParameter,
                                           "hasParameterSolution": BIGOWL.namespace.hasParameter,
                                           "hasImplementation": BIGOWL.namespace.hasImplementation,
                                           "specifiesOutputClass": BIGOWL.namespace.specifiesOutputClass,
                                           "specifiesInputClass": BIGOWL.namespace.specifiesInputClass,
                                           "hasSolution": BIGOWL.namespace.hasSolutionComponent,
                                           "type": RDF.namespace.type,
                                           "label": RDFS.label},
                              {"hasParameter": TITAN.namespace.parameter_operator_name,
                               "hasParameterType": TITAN.namespace.parameter_evaluation_type,
                               "hasParameterSolution": TITAN.namespace.parameter_solution_type,
                               "hasImplementation": TITAN.namespace.ImplementationEvaluation,
                               "specifiesOutputClass": TITAN.namespace.DataEvaluation,
                               "specifiesInputClass": TITAN.namespace.DataSolution,
                               "hasSolution": BIGOWL.namespace.GenericSolution,
                               "type": BIGOWL.namespace.Evaluation,
                               "label": rdflib.Literal('Evaluation', datatype=XSD.string)})

ReplacementComponent = component(TITAN.uri, {"hasParameter": BIGOWL.namespace.hasParameter,
                                           "hasParameterType": BIGOWL.namespace.hasParameter,
                                           "hasParameterSolution": BIGOWL.namespace.hasParameter,
                                           "hasImplementation": BIGOWL.namespace.hasImplementation,
                                           "specifiesInputClass": BIGOWL.namespace.specifiesInputClass,
                                           "specifiesOutputClass": BIGOWL.namespace.specifiesOutputClass,
                                           "hasSolution": BIGOWL.namespace.hasSolutionComponent,
                                           "type": RDF.namespace.type,
                                           "label": RDFS.label},
                              {"hasParameter": TITAN.namespace.parameter_operator_name,
                               "hasParameterType": TITAN.namespace.parameter_replacement_type,
                               "hasParameterSolution": TITAN.namespace.parameter_solution_type,
                               "hasImplementation": TITAN.namespace.ImplementationReplacement,
                               "specifiesInputClass": TITAN.namespace.DataEvaluation,
                               "specifiesOutputClass": TITAN.namespace.DataReplacement,
                               "hasSolution": BIGOWL.namespace.GenericSolution,
                               "type": BIGOWL.namespace.Replacement,
                               "label": rdflib.Literal('Replacement', datatype=XSD.string)})

SolutionCreationComponent = component(TITAN.uri, {"hasParameter": BIGOWL.namespace.hasParameter,
                                           "hasParameterType": BIGOWL.namespace.hasParameter,
                                           "hasParameterSolution": BIGOWL.namespace.hasParameter,
                                           "hasParameterSize": BIGOWL.namespace.hasParameter,
                                           "hasImplementation": BIGOWL.namespace.hasImplementation,
                                           "specifiesOutputClass": BIGOWL.namespace.specifiesOutputClass,
                                           "hasSolution": BIGOWL.namespace.hasSolutionComponent,
                                           "type": RDF.namespace.type,
                                           "label": RDFS.label},
                              {"hasParameter": TITAN.namespace.parameter_operator_name,
                               "hasParameterType": TITAN.namespace.parameter_creation_type,
                               "hasParameterSolution": TITAN.namespace.parameter_solution_type,
                               "hasParameterSize": TITAN.namespace.parameter_population_size,
                               "hasImplementation": TITAN.namespace.ImplementationSolutionsCreation,
                               "specifiesOutputClass": TITAN.namespace.DataSolution,
                               "hasSolution": BIGOWL.namespace.GenericSolution,
                               "type": BIGOWL.namespace.SolutionCreation,
                               "label": rdflib.Literal('Solution Creation', datatype=XSD.string)})

TerminationComponent = component(TITAN.uri, {"hasParameter": BIGOWL.namespace.hasParameter,
                                           "hasParameterType": BIGOWL.namespace.hasParameter,
                                           "hasParameterSolution": BIGOWL.namespace.hasParameter,
                                           "hasImplementation": BIGOWL.namespace.hasImplementation,
                                           "specifiesInputClassEvaluation": BIGOWL.namespace.specifiesInputClass,
                                           "specifiesInputClassReplacement": BIGOWL.namespace.specifiesInputClass,
                                           "specifiesOutputClass": BIGOWL.namespace.specifiesOutputClass,
                                           "hasSolution": BIGOWL.namespace.hasSolutionComponent,
                                           "type": RDF.namespace.type,
                                           "label": RDFS.label},
                              {"hasParameter": TITAN.namespace.parameter_operator_name,
                               "hasParameterType": TITAN.namespace.parameter_termination_type,
                               "hasParameterSolution": TITAN.namespace.parameter_solution_type,
                               "hasImplementation": TITAN.namespace.ImplementationTermination,
                               "specifiesInputClassEvaluation": TITAN.namespace.DataEvaluation,
                               "specifiesInputClassReplacement": TITAN.namespace.DataReplacement,
                               "specifiesOutputClass": TITAN.namespace.DataTermination,
                               "hasSolution": BIGOWL.namespace.GenericSolution,
                               "type": BIGOWL.namespace.Termination,
                               "label": rdflib.Literal('Termination', datatype=XSD.string)})

VariationComponent = component(TITAN.uri, {"hasParameter": BIGOWL.namespace.hasParameter,
                                           "hasParameterType": BIGOWL.namespace.hasParameter,
                                           "hasParameterSolution": BIGOWL.namespace.hasParameter,
                                           "hasParameterOffspring": BIGOWL.namespace.hasParameter,
                                           "hasImplementation": BIGOWL.namespace.hasImplementation,
                                           "hasParameterCrossoverProbability": BIGOWL.namespace.hasParameter,
                                           "hasParameterCrossoverDistribution": BIGOWL.namespace.hasParameter,
                                           "hasParameterMutationProbability": BIGOWL.namespace.hasParameter,
                                           "hasParameterMutationDistribution": BIGOWL.namespace.hasParameter,
                                           "specifiesInputClass": BIGOWL.namespace.specifiesInputClass,
                                           "specifiesOutputClass": BIGOWL.namespace.specifiesOutputClass,
                                           "hasSolution": BIGOWL.namespace.hasSolutionComponent,
                                           "type": RDF.namespace.type,
                                           "label": RDFS.label},
                              {"hasParameter": TITAN.namespace.parameter_operator_name,
                               "hasParameterType": TITAN.namespace.parameter_variation_type,
                               "hasParameterSolution": TITAN.namespace.parameter_solution_type,
                               "hasParameterOffspring": TITAN.namespace.parameter_offspring_population_size,
                               "hasImplementation": TITAN.namespace.ImplementationVariation,
                               "specifiesInputClass": TITAN.namespace.DataSelection,
                               "specifiesOutputClass": TITAN.namespace.DataSolution,
                               "hasParameterCrossoverProbability": TITAN.namespace.parameter_crossover_probability,
                               "hasParameterCrossoverDistribution": TITAN.namespace.parameter_crossover_distribution_index,
                               "hasParameterMutationProbability": TITAN.namespace.parameter_mutation_probability,
                               "hasParameterMutationDistribution": TITAN.namespace.parameter_mutation_distribution_index,
                               "hasSolution": BIGOWL.namespace.GenericSolution,
                               "type": BIGOWL.namespace.Variation,
                               "label": rdflib.Literal('Variation', datatype=XSD.string)})

CrossoverComponent = component(TITAN.uri, {"hasParameter": BIGOWL.namespace.hasParameter,
                                           "hasParameterType": BIGOWL.namespace.hasParameter,
                                           "hasParameterSolution": BIGOWL.namespace.hasParameter,
                                           "hasParameterProbability": BIGOWL.namespace.hasParameter,
                                           "hasImplementation": BIGOWL.namespace.hasImplementation,
                                           "specifiesOutputClass": BIGOWL.namespace.specifiesOutputClass,
                                           "hasSolution": BIGOWL.namespace.hasSolutionComponent,
                                           "type": RDF.namespace.type,
                                           "label": RDFS.label},
                              {"hasParameter": TITAN.namespace.parameter_operator_name,
                               "hasParameterType": TITAN.namespace.parameter_crossover_type,
                               "hasParameterSolution": TITAN.namespace.parameter_solution_type,
                               "hasParameterProbability": TITAN.namespace.parameter_crossover_probability,
                               "hasImplementation": TITAN.namespace.ImplementationCrossover,
                               "specifiesOutputClass": TITAN.namespace.DataCrossover,
                               "hasSolution": BIGOWL.namespace.GenericSolution,
                               "type": BIGOWL.namespace.Crossover,
                               "label": rdflib.Literal('Crossover', datatype=XSD.string)})

MutationComponent = component(TITAN.uri, {"hasParameter": BIGOWL.namespace.hasParameter,
                                           "hasParameterType": BIGOWL.namespace.hasParameter,
                                           "hasParameterSolution": BIGOWL.namespace.hasParameter,
                                           "hasParameterProbability": BIGOWL.namespace.hasParameter,
                                           "hasImplementation": BIGOWL.namespace.hasImplementation,
                                           "specifiesOutputClass": BIGOWL.namespace.specifiesOutputClass,
                                           "hasSolution": BIGOWL.namespace.hasSolutionComponent,
                                           "type": RDF.namespace.type,
                                           "label": RDFS.label},
                              {"hasParameter": TITAN.namespace.parameter_operator_name,
                               "hasParameterType": TITAN.namespace.parameter_mutation_type,
                               "hasParameterSolution": TITAN.namespace.parameter_solution_type,
                               "hasParameterProbability": TITAN.namespace.parameter_mutation_probability,
                               "hasImplementation": TITAN.namespace.ImplementationMutation,
                               "specifiesOutputClass": TITAN.namespace.DataMutation,
                               "hasSolution": BIGOWL.namespace.GenericSolution,
                               "type": BIGOWL.namespace.Mutation,
                               "label": rdflib.Literal('Mutation', datatype=XSD.string)})

RankingComponent = component(TITAN.uri, {"hasParameter": BIGOWL.namespace.hasParameter,
                                           "hasParameterType": BIGOWL.namespace.hasParameter,
                                           "hasParameterSolution": BIGOWL.namespace.hasParameter,
                                           "hasImplementation": BIGOWL.namespace.hasImplementation,
                                           "specifiesOutputClass": BIGOWL.namespace.specifiesOutputClass,
                                           "hasSolution": BIGOWL.namespace.hasSolutionComponent,
                                           "type": RDF.namespace.type,
                                           "label": RDFS.label},
                              {"hasParameter": TITAN.namespace.parameter_operator_name,
                               "hasParameterType": TITAN.namespace.parameter_ranking_type,
                               "hasParameterSolution": TITAN.namespace.parameter_solution_type,
                               "hasImplementation": TITAN.namespace.ImplementationRanking,
                               "specifiesOutputClass": TITAN.namespace.DataRanking,
                               "hasSolution": BIGOWL.namespace.GenericSolution,
                               "type": BIGOWL.namespace.Ranking,
                               "label": rdflib.Literal('Ranking', datatype=XSD.string)})

DensityEstimatorComponent = component(TITAN.uri, {"hasParameter": BIGOWL.namespace.hasParameter,
                                           "hasParameterType": BIGOWL.namespace.hasParameter,
                                           "hasParameterSolution": BIGOWL.namespace.hasParameter,
                                           "hasImplementation": BIGOWL.namespace.hasImplementation,
                                           "specifiesOutputClass": BIGOWL.namespace.specifiesOutputClass,
                                           "hasSolution": BIGOWL.namespace.hasSolutionComponent,
                                           "type": RDF.namespace.type,
                                           "label": RDFS.label},
                              {"hasParameter": TITAN.namespace.parameter_operator_name,
                               "hasParameterType": TITAN.namespace.parameter_density_estimator_type,
                               "hasParameterSolution": TITAN.namespace.parameter_solution_type,
                               "hasImplementation": TITAN.namespace.ImplementationDensityEstimator,
                               "specifiesOutputClass": TITAN.namespace.DataDensityEstimator,
                               "hasSolution": BIGOWL.namespace.GenericSolution,
                               "type": BIGOWL.namespace.DensityEstimator,
                               "label": rdflib.Literal('Density Estimator', datatype=XSD.string)})

EvolutionaryAlgorithmComponent = component(TITAN.uri, {"specifiesInputClassSelection": BIGOWL.namespace.specifiesInputClass,
                                           "specifiesInputClassVariation": BIGOWL.namespace.specifiesInputClass,
                                           "specifiesInputClassEvaluation": BIGOWL.namespace.specifiesInputClass,
                                           "specifiesInputClassSolutionCreator": BIGOWL.namespace.specifiesInputClass,
                                           "specifiesInputClassReplacement": BIGOWL.namespace.specifiesInputClass,
                                           "specifiesInputClassTermination": BIGOWL.namespace.specifiesInputClass,
                                           "hasImplementation": BIGOWL.namespace.hasImplementation,
                                           "specifiesOutputClassFUN": BIGOWL.namespace.specifiesOutputClass,
                                           "specifiesOutputClassVAR": BIGOWL.namespace.specifiesOutputClass,
                                           "hasSolution": BIGOWL.namespace.hasSolutionComponent,
                                           "type": RDF.namespace.type,
                                           "label": RDFS.label},
                              {"specifiesInputClassSelection": TITAN.namespace.DataSelection,
                               "specifiesInputClassVariation": TITAN.namespace.DataVariation,
                               "specifiesInputClassEvaluation": TITAN.namespace.DataEvaluation,
                               "specifiesInputClassSolutionCreator": TITAN.namespace.DataSolutionCreator,
                               "specifiesInputClassReplacement": TITAN.namespace.DataReplacement,
                               "specifiesInputClassTermination": TITAN.namespace.DataTermination,
                               "hasImplementation": TITAN.namespace.ImplementationEvolutionaryAlgorithm,
                               "specifiesOutputClassFUN": TITAN.namespace.FUN,
                               "specifiesOutputClassVAR": TITAN.namespace.VAR,
                               "hasSolution": BIGOWL.namespace.GenericSolution,
                               "type": BIGOWL.namespace.EvolutionaryAlgorithm,
                               "label": rdflib.Literal('Evolutionary Algorithm', datatype=XSD.string)})