
CREATE PROCEDURE SP_INSERT_BENEFICIARIOANS (  
 @p_beneficiario_Id bigint ,  
 @p_cco bigint ,  
 @p_situacao varchar (255),  
 @p_dataAtualizacao varchar(255) ,  
 @p_conferencia_Id bigint ,  
 @p_logradouro varchar (255),  
 @p_numero varchar (255),  
 @p_complemento varchar (255),  
 @p_bairro varchar (255),  
 @p_codigoMunicipio int ,  
 @p_codigoMunicipioResidencia int ,  
 @p_cep int ,  
 @p_resideExterior tinyint ,  
 @p_tipoEndereco tinyint ,  
 @p_cpf bigint ,  
 @p_cns bigint ,  
 @p_nome varchar (255),  
 @p_sexo tinyint ,  
 @p_dataNascimento date ,  
 @p_nomeMae varchar (255),  
 @p_ccoBeneficiarioTitular bigint ,  
 @p_cnpjEmpresaContratante bigint ,  
 @p_codigoBeneficiario varchar (255),  
 @p_dataCancelamento varchar(255) ,  
 @p_datacontratacao varchar(255) ,  
 @p_itensExcluidosCobertura tinyint ,  
 @p_motivoCancelamento tinyint ,  
 @p_numeroPlanoANS int ,  
 @p_relacaoDependencia tinyint ,  
 @p_competencia date  
)  
AS   
 BEGIN   
   BEGIN TRY 
	BEGIN TRAN 
	  INSERT INTO BENEFICIARIOANS(  
		BENEFICIARIO_ID,  
		CCO,  
		SITUACAO,  
		dataAtualizacao,  
		CONFERENCIA_ID,  
		LOGRADOURO,  
		NUMERO,  
		COMPLEMENTO,  
		BAIRRO,  
		codigoMunicipio,  
		codigoMunicipioResidencia,  
		CEP,  
		resideExterior,  
		tipoEndereco,  
		CPF,  
		CNS,  
		NOME,  
		SEXO,  
		dataNascimento,  
		nomeMae,  
		ccoBeneficiarioTitular,  
		cnpjEmpresaContratante,  
		codigoBeneficiario,  
		dataCancelamento,  
		datacontratacao,  
		itensExcluidosCobertura,  
		motivoCancelamento,  
		numeroPlanoANS,  
		relacaoDependencia,  
		COMPETENCIA  
	  )  
	  VALUES (@p_BENEFICIARIO_ID,  
		@p_CCO,  
		@p_SITUACAO,  
		@p_dataAtualizacao,  
		@p_CONFERENCIA_ID,  
		NULLIF(@p_LOGRADOURO, 'nan'),  
		NULLIF(@p_NUMERO, '0'),  
		NULLIF(@p_COMPLEMENTO, 'nan'),  
		NULLIF(@p_BAIRRO, 'nan'),  
		NULLIF(@p_codigoMunicipio, 0),  
		NULLIF(@p_codigoMunicipioResidencia, 0),  
		NULLIF(@p_CEP, 0),  
		NULLIF(@p_resideExterior, 0),  
		NULLIF(CAST(@p_tipoEndereco AS VARCHAR(10)), 'nan'),  
		NULLIF(@p_CPF, 0),  
		NULLIF(@p_CNS, 0),  
		NULLIF(@p_NOME, 'nan'),  
		NULLIF(CAST(@p_SEXO AS VARCHAR(10)), 'nan'),  
		@p_dataNascimento,  
		NULLIF(@p_nomeMae, 'nan'),  
		NULLIF(@p_ccoBeneficiarioTitular, 0),  
		NULLIF(@p_cnpjEmpresaContratante, 0),  
		@p_codigoBeneficiario,  
		NULLIF(@p_dataCancelamento, 'nan'),  
		NULLIF(@p_datacontratacao, 'nan'),  
		NULLIF(CAST(@p_itensExcluidosCobertura AS VARCHAR(10)), 'nan'),  
		NULLIF(@p_motivoCancelamento, 0),  
		NULLIF(@p_numeroPlanoANS, 0),  
		NULLIF(@p_relacaoDependencia, 0),  
		@p_COMPETENCIA)  
	COMMIT TRAN 
	END TRY 
	BEGIN CATCH
		ROLLBACK;
		THROW;
		
	END CATCH 
 END  
  