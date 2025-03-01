package com.example.atmconsultoria

import android.content.Intent
import android.os.Bundle
import android.util.Half
import android.util.Log
import android.view.View
import android.widget.Button
import android.widget.ImageButton
import android.widget.Toast
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class MainActivity : AppCompatActivity() {
    var btnClientes : ImageButton? = null
    var btnContato : ImageButton? = null
    var btnEmpresa : ImageButton? = null
    var btnServicos : ImageButton? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)

        mainConfig()

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }
    }

    fun mainConfig() {
        btnClientes = findViewById<ImageButton>(R.id.btnClientes)
        btnContato = findViewById<ImageButton>(R.id.btnContato)
        btnEmpresa = findViewById<ImageButton>(R.id.btnEmpresa)
        btnServicos = findViewById<ImageButton>(R.id.btnServicos)
        listeners()
    }

    fun listeners() {
        btnClientes?.setOnClickListener() {
            Toast.makeText(this, "Tela dos Clientes", Toast.LENGTH_LONG).show()
            val VAR = Intent(this, ClientesActivity::class.java)
            startActivity(VAR)
        }

        btnContato?.setOnClickListener() {
            Toast.makeText(this, "Tela dos Contatos", Toast.LENGTH_LONG).show()
            val VAR = Intent(this, ContatoActivity::class.java)
            startActivity(VAR)
        }

        btnEmpresa?.setOnClickListener() {
            Toast.makeText(this, "Tela das Empresas", Toast.LENGTH_LONG).show()
            val VAR = Intent(this, EmpresaActivity::class.java)
            startActivity(VAR)
        }

        btnServicos?.setOnClickListener() {
            Toast.makeText(this, "Tela dos Serviços", Toast.LENGTH_LONG).show()
            val VAR = Intent(this, ServicoActivity::class.java)
            startActivity(VAR)
        }
    }

}