SELECT  
    relatorio_cad_op.*, 
    demonstracoes_contabeis.*, 
    CAST(vl_saldo_final AS DECIMAL(15,2)) - CAST(vl_saldo_inicial AS DECIMAL(15,2)) AS despesa
FROM relatorio_cad_op  
JOIN demonstracoes_contabeis  
    ON relatorio_cad_op.registro_ans = demonstracoes_contabeis.reg_ans 
WHERE demonstracoes_contabeis.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  NA MODALIDADE DE PAGAMENTO POR CAPITATION'
ORDER BY despesa DESC
LIMIT 10;
