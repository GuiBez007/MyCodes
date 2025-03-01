package com.example.minhaterceiratentativa

import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import kotlin.random.Random
import androidx.lifecycle.lifecycleScope
import kotlinx.coroutines.launch
import kotlinx.coroutines.delay


class MainActivity : AppCompatActivity() {
    private lateinit var textView4: TextView
    private val listaFrases = arrayOf(
        "Isso não estava no contrato!",
        "Por que tem um pato na sala?",
        "Eu achei que era chocolate!",
        "Quem desligou a gravidade?",
        "Só se for na casa do meu primo!",
        "Eu nunca disse que sabia pilotar.",
        "Cuidado com o abacaxi!",
        "A geladeira está cantando de novo.",
        "Por que tem um alien na varanda?",
        "Isso não é meu cachorro.",
        "Eu sempre quis ser um pirata.",
        "O queijo fugiu da pizza!",
        "Quem colocou glitter na sopa?",
        "A lua está no modo avião.",
        "Eu sonhei que era um pão de queijo.",
        "Quem convidou o urso?",
        "Eu achei que era uma cenoura gigante.",
        "Por que tem uma girafa no elevador?",
        "Meu tênis pediu demissão.",
        "Isso é um hambúrguer ou um chapéu?"
    )

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        textView4 = findViewById(R.id.textView4) as TextView
    }

    fun sortearFrase(view: View) {
//        LogCat -> // Log.i("BOTAO","pressionado!")
//        var lblTeste = findViewById(R.id.lblTeste) as TextView
//        lblTeste.setText("Uau, sabe ler!")


//        var lblTexto2 = findViewById(R.id.lblTexto2) as TextView
//        var numero = Random.nextInt(11)
//
//        lblTexto2.setText("O número sorteado foi $numero")
//
        // Funciona como o Thread.sleep do Java, porém não para toda a aplicação
        lifecycleScope.launch {
            delay(3000)
            textView4.setText("Nenhum número selecionado")
        }

        textView4.setText(listaFrases[Random.nextInt(listaFrases.size)])

    }
}